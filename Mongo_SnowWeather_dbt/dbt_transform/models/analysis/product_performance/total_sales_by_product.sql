-- models/product_performance/total_sales_by_product.sql
WITH product_sales AS (
    SELECT p.PRODUCT_ID, p.PRODUCT_NAME, p.CATEGORY, SUM(o.TOTAL_AMOUNT) AS total_sales
    FROM {{ ref('src_products') }} p
    JOIN {{ ref('src_orders') }} o ON p.PRODUCT_ID = o.PRODUCT_ID
    GROUP BY p.PRODUCT_ID, p.PRODUCT_NAME, p.CATEGORY
)
SELECT *
FROM product_sales
