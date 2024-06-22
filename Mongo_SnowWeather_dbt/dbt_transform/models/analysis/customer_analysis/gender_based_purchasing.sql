-- models/customer_analysis/gender_based_purchasing.sql
WITH customer_orders AS (
    SELECT c.GENDER, SUM(o.TOTAL_AMOUNT) AS total_spent
    FROM {{ ref('src_customers') }} c
    JOIN {{ ref('src_orders') }} o ON c.CUSTOMER_ID = o.CUSTOMER_ID
    GROUP BY c.GENDER
)
SELECT *
FROM customer_orders
