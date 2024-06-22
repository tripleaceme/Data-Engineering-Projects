-- models/financial_metrics/profit_analysis.sql
WITH profit_calculations AS (
    SELECT CUSTOMER_ID, PRODUCT_ID, TOTAL_AMOUNT, COST_PRICE,
           (TOTAL_AMOUNT - COST_PRICE) AS profit
    FROM {{ ref('src_orders') }}
)
SELECT *
FROM profit_calculations
