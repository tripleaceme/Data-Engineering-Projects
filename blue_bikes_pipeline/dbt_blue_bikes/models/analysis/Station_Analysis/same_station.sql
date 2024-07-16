with same_station as (

    select 
    case when start_station_id = end_station_id then 'Round Trip' else 'One Way' end ride_type,
    count(*) as total_rides, sum(pricing) as total_revenue, avg(pricing) as avg_rev
    from {{ ref('insight_data') }}
    group by 1
)

select *
from same_station