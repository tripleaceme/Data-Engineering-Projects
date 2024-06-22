-- models/customer_analysis/age_group_distribution.sql
WITH customer_data AS (
    SELECT AGE_GROUP, COUNT(*) AS num_customers
    FROM {{ ref('src_customers') }}
    GROUP BY AGE_GROUP
)
SELECT *
FROM customer_data
