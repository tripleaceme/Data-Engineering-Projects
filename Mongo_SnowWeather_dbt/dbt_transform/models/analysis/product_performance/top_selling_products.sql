-- models/product_performance/top_selling_products.sql
WITH top_products AS (
    SELECT CATEGORY, PRODUCT_NAME, SUM(o.TOTAL_AMOUNT) AS total_sales
    FROM {{ ref('src_products') }} p
    JOIN {{ ref('src_orders') }} o ON p.PRODUCT_ID = o.PRODUCT_ID
    GROUP BY CATEGORY, PRODUCT_NAME
    ORDER BY total_sales DESC
    LIMIT 10
)
SELECT *
FROM top_products
