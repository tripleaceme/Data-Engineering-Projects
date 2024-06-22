# MarketEase Snowflake Data Analysis with dbt

## Overview

MarketEase, an e-commerce company, has migrated its data infrastructure to Snowflake to enhance its data analytics capabilities. This repository contains the dbt (Data Build Tool) project aimed at transforming and analyzing MarketEase's data for various analytical goals.

## Objectives

The primary objectives of this dbt project are aligned with MarketEase's goals:

1. **Customer Analysis:**
   - Understanding customer demographics, geographical distribution, and purchasing behavior.

2. **Product Performance Analysis:**
   - Evaluating product sales, ratings, and reviews to identify top-performing products and categories.

3. **Order Management:**
   - Monitoring order statuses, analyzing order cancellations, processing times, and financial metrics.

## Project Structure

The dbt project is structured as follows:

```
dbt_project/
├── models/
|   |── analysis/
│   ├──── customer_analysis/
│   │       ├── age_group_distribution.sql
│   │       ├── geographical_distribution.sql
│   │       ├── gender_based_purchasing.sql
│   │       ├── avg_order_value_per_customer.sql
│   │       ├── frequency_of_purchases.sql
│   │       ├── high_value_customers.sql
│   │       ├── customer_analysis.yml
│   ├──── product_performance/
│   │       ├── total_sales_by_product.sql
│   │       ├── product_ratings_and_reviews.sql
│   │       ├── top_selling_products.sql
│   │       ├── product_performance.yml
│   ├──── order_management/
│   │       ├── order_status_proportion.sql
│   │       ├── temporal_order_patterns.sql
│   │       ├── weekday_weekend_orders.sql
│   │       ├── order_management.yml
│   ├──── financial_metrics/
│   │       ├── total_revenue.sql
│   │       ├── profit_analysis.sql
│   │       ├── financial_metrics.yml
├── sources/
│   ├── sources.yml
│   ├── customers.yml
│   ├── orders.yml
│   ├── products.yml
│   ├── scr_customers.sql
│   ├── scr_orders.sql
│   ├── scr_products.sql
├── dbt_project.yml
├── profiles.yml
```

### Explanation of Folders and Files

- **models/**: Contains dbt model files organized by analytical goals (customer analysis, product performance, order management, financial metrics).
- **sources/**: Configuration for source tables (`sources.yml`) used in dbt models.
- **dbt_project.yml**: Configuration file specifying project metadata and model configurations.
- **profiles.yml**: Snowflake connection details for dbt.

## Example dbt Model Files

Here are examples of dbt model files corresponding to each analytical goal:

### Customer Analysis

#### age_group_distribution.sql

```sql
-- models/customer_analysis/age_group_distribution.sql
WITH customer_data AS (
    SELECT AGE_GROUP, COUNT(*) AS num_customers
    FROM {{ ref('src_customers') }}
    GROUP BY AGE_GROUP
)
SELECT *
FROM customer_data;
```

### Product Performance

#### total_sales_by_product.sql

```sql
-- models/product_performance/total_sales_by_product.sql
WITH product_sales AS (
    SELECT p.PRODUCT_ID, p.PRODUCT_NAME, p.CATEGORY, SUM(o.TOTAL_AMOUNT) AS total_sales
    FROM {{ ref('src_products') }} p
    JOIN {{ ref('src_orders') }} o ON p.PRODUCT_ID = o.PRODUCT_ID
    GROUP BY p.PRODUCT_ID, p.PRODUCT_NAME, p.CATEGORY
)
SELECT *
FROM product_sales;
```

### Order Management

#### order_status_proportion.sql

```sql
-- models/order_management/order_status_proportion.sql
WITH order_status_counts AS (
    SELECT STATUS, COUNT(*) AS num_orders
    FROM {{ ref('src_orders') }}
    GROUP BY STATUS
)
SELECT *
FROM order_status_counts;
```

### Financial Metrics

#### total_revenue.sql

```sql
-- models/financial_metrics/total_revenue.sql
WITH revenue_metrics AS (
    SELECT SUM(TOTAL_AMOUNT) AS total_revenue, AVG(TOTAL_AMOUNT) AS avg_order_value
    FROM {{ ref('src_orders') }}
)
SELECT *
FROM revenue_metrics;
```

## Getting Started

To replicate or extend this dbt project:

1. Clone this repository to your local machine.
2. Configure `profiles.yml` with your Snowflake connection details.
3. Customize `sources.yml` in the `sources/` folder to reflect your specific database schema and tables.
4. Explore and modify dbt model files (`models/`) to suit your specific analytical requirements.
5. Use `dbt run` and `dbt test` commands to build and test your dbt models.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or additions.