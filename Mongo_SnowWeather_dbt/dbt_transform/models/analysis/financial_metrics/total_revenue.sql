-- models/financial_metrics/total_revenue.sql
WITH revenue_metrics AS (
    SELECT SUM(TOTAL_AMOUNT) AS total_revenue, AVG(TOTAL_AMOUNT) AS avg_order_value
    FROM {{ ref('src_orders') }}
)
SELECT *
FROM revenue_metrics
