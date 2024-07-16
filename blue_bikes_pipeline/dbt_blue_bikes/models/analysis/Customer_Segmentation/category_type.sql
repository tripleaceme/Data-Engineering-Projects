with category_type as(
    
    select member_casual, category, 
    sum(pricing) as total_rev,
    count(*) total_rides
    from {{ ref('insight_data') }}
    group by 1, 2
)


select *
from category_type