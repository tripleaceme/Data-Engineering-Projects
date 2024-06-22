-- models/customer_analysis/frequency_of_purchases.sql
WITH customer_purchase_frequency AS (
    SELECT c.AGE_GROUP, c.STATE_CODE, COUNT(o.ORDER_DATE) AS num_purchases
    FROM {{ ref('src_customers') }} c
    JOIN {{ ref('src_orders') }} o ON c.CUSTOMER_ID = o.CUSTOMER_ID
    GROUP BY c.AGE_GROUP, c.STATE_CODE
)
SELECT *
FROM customer_purchase_frequency
