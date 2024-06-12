from pymongo import MongoClient
import pandas as pd
from sqlalchemy import create_engine
import configparser as cf

# configure api credential
parser = cf.ConfigParser()
parser.read('cred.conf')

# Database connection details
host = parser.get('mysql_creds_updated_updated','host')
password = parser.get('mysql_creds_updated','password')
user = parser.get('mysql_creds_updated','user')
database = parser.get('mysql_creds_updated','database')

db_url = f"mysql+pymysql://{user}:{password}@{host}/{database}"
engine = create_engine(db_url)

# Store data in MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["sales_oltp_db"]

# Extract data from MongoDB
customers = list(db.customers.find())
products = list(db.products.find())
orders = list(db.orders.find())


customers_df = pd.DataFrame(customers)
products_df = pd.DataFrame(products)
orders_df = pd.DataFrame(orders)

print('Customers Columns')
print(customers_df.columns)
print()

print('Products Columns')
print(products_df.columns)
print()

print('Orders Columns')
print(orders_df.columns)
print()