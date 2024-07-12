import os
import requests
import zipfile
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from datetime import datetime as dt

# Snowflake connection configuration
SNOWFLAKE_USER = '#'
SNOWFLAKE_PASSWORD = '#'
SNOWFLAKE_ACCOUNT_URL = '#' #'your_account_name.your_region'
SNOWFLAKE_WAREHOUSE = 'DATAMONGER_WH'
SNOWFLAKE_DATABASE = 'project_data'
SNOWFLAKE_SCHEMA = 'bikes'


# Create a connection URL
db_url = URL(
    account=SNOWFLAKE_ACCOUNT_URL,
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)

# Create an SQLAlchemy engine
engine = create_engine(db_url)


# directory to store raw and combined data
raw_data_dir = 'Data-Engineering-Projects/blue_bikes_pipeline/data/raw_data'

# Ensure the directories exist
os.makedirs(raw_data_dir, exist_ok=True)


#================================ RIDES DATA =======================================================
# Generate URLs for the specified months
#year_month_list = [f"{year}{month:02d}" for year in range(2022, 2024) for month in range(1, 13)]
year_month_list = [f"2024{month:02d}" for month in range(1, 7)]
urls = [f"https://s3.amazonaws.com/hubway-data/{ym}-bluebikes-tripdata.zip" for ym in year_month_list]

# Download and unzip the files
for url in urls:
    # Download the zip file
    response = requests.get(url)
    zip_path = os.path.join(raw_data_dir, os.path.basename(url))
    with open(zip_path, 'wb') as f:
        f.write(response.content)
    
    # Unzip the file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(raw_data_dir)
    
    # Delete the zip file
    os.remove(zip_path)

# Read all CSV files
csv_files = [os.path.join(raw_data_dir, f) for f in os.listdir(raw_data_dir) if f.endswith('.csv')]
rides_count = 0

for file in csv_files:

    # Read the saved DataFrame
    raw_blue_bikes = pd.read_csv(file)

    # Select usable columns
    bikes_df = raw_blue_bikes[['rideable_type', 'started_at', 'ended_at', 'start_station_id', 'end_station_id', 'member_casual']]
    
    # Number of rows

    rides_count += len(bikes_df)

    # Store transformed bikes data into Snowflake
    load_start_time = dt.now()

    # Batch insert to avoid exceeding maximum expression limit
    batch_size = 100000 
    for i in range(0, len(bikes_df), batch_size):
        batch = bikes_df.iloc[i:i + batch_size]
        batch.to_sql('rides', engine, if_exists='append', index=False)

# Calculate loading duration in minutes
load_end_time = dt.now()

# Convert duration to minutes
load_duration = (load_end_time - load_start_time).total_seconds() / 60 


#================================ STATION DATA =======================================================
station_url = 'https://lyft-lastmile-production-iad.s3.amazonaws.com/static/blue-bikes/current_bluebikes_stations.csv?version=2'
stations = pd.read_csv(station_url, skiprows=1)
stations.drop('Station ID (to match to historic system data)', axis=1, inplace=True)


# Rename the column
stations.rename(columns={'Number': 'station_id', 'NAME': 'station_name',  'Lat':'latitude','Long':'longitude' ,
                         'Seasonal Status': 'seasonal_status' ,'Municipality': 'municipality' ,
                         'Total Docks': 'total_docks' }, inplace=True)

# Remove TBD - upcoming install stations
stations = stations[stations['station_id'] != 'TBD - upcoming install']

# Convert Total Docks to int from float
stations['total_docks'] = stations['total_docks'].astype('int')

# Store transformed stations data into Snowflake
stations.to_sql('stations', engine, if_exists='append', index=False)


#================================ LOG DATA =======================================================

# Get the number of rows in the station DataFrame
station_count = len(stations)

# Get the current date and time
load_date = dt.now()

# Create a DataFrame to log the loading date and number of rows
loading_log = pd.DataFrame({
   'loading_date': [load_date],
   'total_rides_loaded': [rides_count],
    'total_stations': [station_count],
    'loading_duration': [load_duration]
})

# Check for duplicates before appending
existing_logs_query = f"""
                        SELECT *
                        FROM bikes.loading_log
                        WHERE loading_date = '{load_date}' 
                        AND total_rides_loaded = {rides_count} 
                        AND total_stations = {station_count}
                        """

existing_logs = pd.read_sql(existing_logs_query, engine)

if existing_logs.empty:
    # Append the log to the 'loading_log' table in the database
    loading_log.to_sql('loading_log', engine, if_exists='append', index=False)
    print(f"Loading log appended successfully.")
else:
    print(f"Duplicate log entry found for {load_date}, {rides_count} and {station_count}. Log not appended.")

# Remove all the CSV files from the raw data folder
for csv_file in csv_files:
    os.remove(csv_file)

 