with average_rev as (

    select category, sum(pricing) as total_revenue
    from {{ ref('insight_data') }}
    group by 1
)

select category, avg(total_revenue) as avg_revenue
from average_rev
group by 1