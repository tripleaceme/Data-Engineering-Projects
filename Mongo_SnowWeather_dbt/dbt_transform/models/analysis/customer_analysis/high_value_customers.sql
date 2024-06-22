-- models/customer_analysis/high_value_customers.sql
WITH high_value_customers AS (
    SELECT c.CUSTOMER_ID, c.FULL_NAME, SUM(o.TOTAL_AMOUNT) AS total_spent
    FROM {{ ref('src_customers') }} c
    JOIN {{ ref('src_orders') }} o ON c.CUSTOMER_ID = o.CUSTOMER_ID
    GROUP BY c.CUSTOMER_ID, c.FULL_NAME
    ORDER BY total_spent DESC
    LIMIT 10
)
SELECT *
FROM high_value_customers
