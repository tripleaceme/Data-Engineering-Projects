from pymongo import MongoClient
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL


# Configure MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
database = client["sales_oltp_db"]


# Snowflake connection configuration
SNOWFLAKE_USER = 'DataMonger'
SNOWFLAKE_PASSWORD = 'Tr1pleac@'
SNOWFLAKE_ACCOUNT_URL = 'rfxlxmq-qi23044' #'your_account_name.your_region'
SNOWFLAKE_WAREHOUSE = 'DATAMONGER_WH'
SNOWFLAKE_DATABASE = 'MONGO_SALES_DATA'
SNOWFLAKE_SCHEMA = 'SALES'

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

# Pull data from MongoDB collections and convert to DataFrames
customers = pd.DataFrame(list(database.customers.find()))
products = pd.DataFrame(list(database.products.find()))
orders = pd.DataFrame(list(database.orders.find()))

# Close the MongoDB connection
client.close()

# Customer data transformation
customers_df = customers[['customer_id', 'name', 'sex', 'residence', 'latitude', 'longitude', 'birthdate']]
customers_df.rename(columns={'name': 'full_name', 'sex': 'gender'}, inplace=True)
customers_df['dob'] = customers_df['birthdate']
customers_df['dob'] = pd.to_datetime(customers_df['dob'])

def gen_classifier(date_of_birth):
    year = date_of_birth.year
    if year <= 1945:
        return 'Silent Generation'
    elif year <= 1964:
        return 'Baby Boomers'
    elif year <= 1980:
        return 'Generation X'
    elif year <= 1996:
        return 'Millennials (Generation Y)'
    elif year <= 2012:
        return 'Generation Z'
    else:
        return 'Generation Alpha'

def state(address):
    state_code = address[-8:-6]
    return state_code

def zip_code(address):
    zip_code = address[-5:]
    return zip_code

customers_df.loc[:, 'age_group'] = customers_df['dob'].apply(gen_classifier)
customers_df.loc[:, 'state_code'] = customers_df['residence'].apply(state)
customers_df.loc[:, 'zip_code'] = customers_df['residence'].apply(zip_code)
customers_df.drop(['dob', 'residence'], axis=1, inplace=True)

# Store transformed customer data into Snowflake
customers_df.to_sql('customers', engine, if_exists='replace', index=False)

# Product data transformation
products_data = products[['product_id', 'name', 'price', 'category', 'ratings', 'reviews']]
products_data.rename(columns={'name': 'product_name'}, inplace=True)

# Store transformed product data into Snowflake
products_data.to_sql('products', engine, if_exists='replace', index=False)

# Orders data transformation
orders_data = orders[['customer_id', 'product_id', 'quantity', 'total_amount', 'order_date', 'status']]
orders_data['order_date'] = pd.to_datetime(orders_data['order_date'])
orders_data['order_month'] = orders_data['order_date'].dt.month_name()
orders_data['order_day'] = orders_data['order_date'].dt.day_name()
day_of_week = orders_data['order_date'].dt.dayofweek
orders_data['isWeekDay'] = day_of_week.apply(lambda x: "Weekend" if x > 4 else "Weekday")

# Store transformed order data into Snowflake
orders_data.to_sql('orders', engine, if_exists='replace', index=False)