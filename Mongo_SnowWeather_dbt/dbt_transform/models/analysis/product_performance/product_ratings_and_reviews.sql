-- models/product_performance/product_ratings_and_reviews.sql
WITH product_feedback AS (
    SELECT PRODUCT_ID, PRODUCT_NAME, RATINGS, REVIEWS
    FROM {{ ref('src_products') }}
    ORDER BY RATINGS DESC
)
SELECT *
FROM product_feedback
