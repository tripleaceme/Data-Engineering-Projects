-- models/customer_analysis/avg_order_value_per_customer.sql
WITH customer_avg_order AS (
    SELECT c.CUSTOMER_ID, c.FULL_NAME, AVG(o.TOTAL_AMOUNT) AS avg_order_value
    FROM {{ ref('src_customers') }} c
    JOIN {{ ref('src_orders') }} o ON c.CUSTOMER_ID = o.CUSTOMER_ID
    GROUP BY c.CUSTOMER_ID, c.FULL_NAME
)
SELECT *
FROM customer_avg_order
