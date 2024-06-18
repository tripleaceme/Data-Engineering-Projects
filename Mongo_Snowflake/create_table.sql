
CREATE OR REPLACE TABLE mongo_sales_data.sales.customers(

    customer_id int primary key,
    full_name varchar(255) not null,
    gender varchar(6) not null,
    latitude FLOAT not null,
    longitude FLOAT not null,
    birthdate DATE not null,
    age_group varchar(50) not null,
    state_code char(2) not null,
    zip_code char(6)
);

CREATE OR REPLACE TABLE mongo_sales_data.sales.orders (
    customer_id int not null,
    product_id int not null,
    quantity int not null,
    total_amount FLOAT not null,
    order_date DATE not null,
    status varchar(20) not null,
    order_month varchar(20) not null,
    order_day varchar(20) not null,
    isWeekDay char(8) not null
);


CREATE OR REPLACE TABLE mongo_sales_data.sales.products (
    product_id int not null,
    product_name int not null,
    price FLOAT not null,
    category varchar(20) not null,
    ratings FLOAT not null,
    reviews INT not null
)