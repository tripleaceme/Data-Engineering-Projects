from pymongo import MongoClient
import pandas as pd
from sqlalchemy import create_engine
import configparser as cf
from datetime import datetime


# configure api credential
parser = cf.ConfigParser()
parser.read('cred.conf')

# Database connection details
host = parser.get('mysql_creds','host')
password = parser.get('mysql_creds','password')
user = parser.get('mysql_creds','user')
database = parser.get('mysql_creds','database')

db_url = f"mysql+pymysql://{user}:{password}@{host}/{database}"
engine = create_engine(db_url)

# Store data in MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["sales_oltp_db"]

# Extract data from MongoDB
customers = list(db.customers.find())
products = list(db.products.find())
orders = list(db.orders.find())

# convert all to DataFrames
customers_df = pd.DataFrame(customers)
products_df = pd.DataFrame(products)
orders_df = pd.DataFrame(orders)


#customer data transformation
customers_data = customers_df[['customer_id', 'name', 'sex', 'residence', 
                                   'latitude', 'longitude', 'birthdate']]

# Convert birthdate column to datetime
customers_data['birthdate'] = pd.to_datetime(customers_data['birthdate'])

# Calculate age
current_date = datetime.now()
customers_data.loc[:, 'age'] = current_date.year - customers_data['birthdate'].dt.year

# remove extremely old and younger folks
customers_data = customers_data[(customers_data['age'] >= 18) & (customers_data['age'] <= 80)]

# Define age groups based on generational cohorts
def generational_group(birthdate):
    year = birthdate.year
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

# Apply generational group function
customers_data['age_group'] = customers_data['birthdate'].apply(generational_group)

def state(state):
    state_name = state[-8:-6]
    return state_name

# Apply state group function
customers_data['state_code'] = customers_data['residence'].apply(state)

def zip_code(state):
    zip_code = state[-5:]
    return zip_code

# Apply zip_code group function
customers_data['zip_code'] = customers_data['residence'].apply(zip_code)

# Remove unneccessary columns
customers_data.drop(['residence','birthdate'], axis=1, inplace=True)


#products data transformation
products_data = products_df[['product_id', 'price', 'category', 'ratings', 'reviews']]


#orders data transformation
orders_data = orders_df[['customer_id', 'product_id', 'quantity', 'total_amount', 'order_date', 'status']]

# Convert birthdate column to datetime
orders_data['order_date'] = pd.to_datetime(orders_data['order_date'])
orders_data['order_month'] = orders_data['order_date'].dt.month_name()
orders_data['order_day'] = orders_data['order_date'].dt.day_name()

# Extract the day of the week (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
day_of_week = orders_data['order_date'].dt.dayofweek

# Apply the condition to each element of the Series
orders_data['isWeekDay'] = day_of_week.apply(lambda x: "Weekend" if x > 4 else "Weekday")

#print(orders_data['isWeekDay'].value_counts())
