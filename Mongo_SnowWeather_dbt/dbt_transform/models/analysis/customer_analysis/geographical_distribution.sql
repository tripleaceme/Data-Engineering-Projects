-- models/customer_analysis/geographical_distribution.sql
WITH customer_data AS (
    SELECT STATE_CODE, ZIP_CODE, COUNT(*) AS num_customers
    FROM {{ ref('src_customers') }}
    GROUP BY STATE_CODE, ZIP_CODE
)
SELECT *
FROM customer_data
