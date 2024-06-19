from pymongo import MongoClient
import pandas as pd
from sqlalchemy import create_engine

# Configure MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
database = client["sales_oltp_db"]

# MySQL connection configuration
db_url = f"mysql+pymysql://data_engineer:training@localhost/analytics_db"
engine = create_engine(db_url)

# Pull data from MongoDB collections and convert to DataFrames
customers = pd.DataFrame(list(database.customers.find()))
products = pd.DataFrame(list(database.products.find()))
orders = pd.DataFrame(list(database.orders.find()))

# Close the MongoDB connection
client.close()

# Customer data transformation
# Select relevant columns for customers
customers_df = customers[['customer_id', 'name', 'sex', 'residence', 'latitude', 'longitude', 'birthdate']]

# Rename columns for better clarity
customers_df.rename(columns={'name': 'full_name', 'sex': 'gender'}, inplace=True)

# Create a copy of birthdate field for further processing
customers_df['dob'] = customers_df['birthdate']

# Convert dob column to datetime format
customers_df['dob'] = pd.to_datetime(customers_df['dob'])

# Function to classify customers into generations based on birth year
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

# Function to extract state code from residence address
def state(address):
    state_code = address[-8:-6]
    return state_code

# Function to extract zip code from residence address
def zip_code(address):
    zip_code = address[-5:]
    return zip_code

# Apply generation classifier to dob and create a new column 'age_group'
customers_df.loc[:, 'age_group'] = customers_df['dob'].apply(gen_classifier)

# Apply state and zip code extraction functions to residence and create new columns
customers_df.loc[:, 'state_code'] = customers_df['residence'].apply(state)
customers_df.loc[:, 'zip_code'] = customers_df['residence'].apply(zip_code)

# Drop unnecessary columns
customers_df.drop(['dob', 'residence'], axis=1, inplace=True)

# Store transformed customer data into MySQL database
customers_df.to_sql('customers', engine, if_exists='replace', index=False)

# Product data transformation
# Select relevant columns for products
products_data = products[['product_id', 'name', 'price', 'category', 'ratings', 'reviews']]

# Rename columns for better clarity
products_data.rename(columns={'name': 'product_name'}, inplace=True)

# Store transformed product data into MySQL database
products_data.to_sql('products', engine, if_exists='replace', index=False)

# Orders data transformation
# Select relevant columns for orders
orders_data = orders[['customer_id', 'product_id', 'quantity', 'total_amount', 'order_date', 'status']]

# Convert order_date column to datetime format
orders_data['order_date'] = pd.to_datetime(orders_data['order_date'])

# Extract month and day names from order_date and create new columns
orders_data['order_month'] = orders_data['order_date'].dt.month_name()
orders_data['order_day'] = orders_data['order_date'].dt.day_name()

# Extract the day of the week (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
day_of_week = orders_data['order_date'].dt.dayofweek

# Determine if the order was placed on a weekday or weekend and create a new column
orders_data['isWeekDay'] = day_of_week.apply(lambda x: "Weekend" if x > 4 else "Weekday")

# Store transformed order data into MySQL database
orders_data.to_sql('orders', engine, if_exists='replace', index=False)
