import pandas as pd


weather_df = pd.read_csv('')


weather_df.to_csv('dbt/seeds/weather.csv', index=False)


import pymongo
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from pymongo import MongoClient
import pandas as pd


#establish data connection to Mongo db
client = MongoClient('mongodb://localhost:27017/')
database = client['Sales_db']
collection = database['Customers']
product_doc = database['Product']

#Get data in Mongo Collection
product_collection = list(product_doc.find())


client.close()

# establish connection to snowflake 
sn_user='ERIC2016NG'
sn_database= 'ECOMMERCE_DB'
sn_schema= 'COMMERCE_SCH'
sn_warehouse='ADVENTURE'
sn_password= 'Dancing123$'
sn_account='iigqjuz-hz91508'

db_url = URL(
    user=sn_user,
    database=sn_database,
    schema=sn_schema,
    warehouse=sn_warehouse,
    password=sn_password,
    account=sn_account
    
)

engine = create_engine(db_url)

product_data = []

for i in product_collection:
   del i['_id']
   product_data.append(i)

df_product = pd.DataFrame(product_data)
print()
df_product.to_sql('product', engine, if_exists='replace', index=False)





