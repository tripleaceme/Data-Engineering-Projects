-- models/order_management/temporal_order_patterns.sql
WITH order_patterns AS (
    SELECT ORDER_MONTH, COUNT(*) AS num_orders,
           SUM(CASE WHEN STATUS = 'Cancelled' THEN 1 ELSE 0 END) AS num_cancelled
    FROM {{ ref('src_orders') }}
    GROUP BY ORDER_MONTH
)
SELECT *
FROM order_patterns
