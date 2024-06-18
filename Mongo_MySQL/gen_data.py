import random
from faker import Faker
from pymongo import MongoClient

# database connection
client = MongoClient("mongodb://localhost:27017/")
database = client["sales_oltp_db"]


# Initialize Faker
fake = Faker()

# Number of data points to generate
num_customers = 150
num_products = 2000
num_orders = 100000


# data storage setup
customers = []
orders = []
products = []
order_status = ['Pending', 'Processing', 'Cancelled', 'Delivered', 'Shipped', 'Refund']


# Generate unique customer IDs
customer_ids = list(range(1, num_customers + 1))
random.shuffle(customer_ids)


# Generate data for 150 customers and store in the customers list
for i in range(num_customers):
    raw_customer = fake.profile()
    modified_customer_data = {}
    
    for key , value in raw_customer.items():

        # convert decimal field to str
        if key == 'current_location' :
            modified_customer_data['latitude'] = str(raw_customer[key][0])
            modified_customer_data['longitude'] = str(raw_customer[key][1])
        
         # convert datetime field to date
        elif key == 'birthdate':
            mod_date = raw_customer[key].strftime("%Y-%m-%d")
            modified_customer_data['birthdate'] = mod_date

        # Store the rest without modification
        else:
            modified_customer_data[key] = value
        
    # Assign a unique customer_id
    modified_customer_data['customer_id'] = customer_ids[i]

    # Add all the data into customers list
    customers.append(modified_customer_data)

# Insert all data into the mongoDB customer document aka table
database.customers.insert_many(customers)


# Generate unique product IDs
product_ids = list(range(1, num_products + 1))
random.shuffle(product_ids)

# Generate data for 2000 products and store in the products list
for i in range(num_products):
    prod_category = ['Electronics', 'Home & Kitchen', 'Movies & Television', 'Clothing', 'Books', 'Beauty & Personal Care']
    product = {
        "product_id": product_ids[i],
        "name": fake.company(),
        "price": round(random.uniform(300.0, 1500.0), 2),
        "description": fake.text(60),
        "category": fake.random_element(prod_category),
        "stock_quantity": random.randint(30, 70),
        "ratings": round(random.uniform(1.0, 5.0), 1),
        "reviews": random.randint(300, 900)
    }
    products.append(product)

# Insert all data into the MongoDB products collection
database.products.insert_many(products)


# Convert products list to a dictionary for easier access
products_dict = {product['product_id']: product for product in products}

# Generate data for 100,000 orders and store in the orders list
for _ in range(num_orders):
    customer_id = random.choice(customer_ids)
    product_id = random.randint(1, num_products)
    quantity = random.randint(2, 10)
    total_amount = products_dict[product_id]['price'] * quantity

    order = {
        "customer_id": customer_id,
        "product_id": product_id,
        "quantity": quantity,
        "total_amount": round(total_amount, 2),
        "order_date": fake.date_between(start_date='-180d'),  # 4 months ago till date.
        "status": fake.random_element(order_status)
    }

    order['order_date'] = order['order_date'].strftime("%Y-%m-%d")

    orders.append(order)

# Insert all data into the MongoDB orders collection
database.orders.insert_many(orders)
