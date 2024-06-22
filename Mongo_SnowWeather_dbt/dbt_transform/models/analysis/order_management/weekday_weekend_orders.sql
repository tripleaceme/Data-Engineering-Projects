-- models/order_management/weekday_weekend_orders.sql
WITH order_trends AS (
    SELECT "isWeekDay" as isWeekDay, COUNT(*) AS num_orders
    FROM {{ ref('src_orders') }}
    GROUP BY isWeekDay
)
SELECT *
FROM order_trends
