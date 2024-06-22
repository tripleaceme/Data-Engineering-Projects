-- models/order_management/order_status_proportion.sql
WITH order_status_counts AS (
    SELECT STATUS, COUNT(*) AS num_orders
    FROM {{ ref('src_orders') }}
    GROUP BY STATUS
)
SELECT *
FROM order_status_counts
