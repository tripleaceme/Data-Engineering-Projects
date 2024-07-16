with revenue as (
    select
        ride_month_2, 
        total_revenue
    from {{ ref('peak_revenue_periods') }}
),
costs as (
    select
        ride_month_2,
        maintenance_cost,
        other_costs,
        maintenance_cost + other_costs as total_cost
    from {{ ref('cost') }}
)

select
    revenue.ride_month_2,
    total_revenue,
    total_cost,
    total_revenue - total_cost as profit,
    (total_revenue - total_cost) / total_revenue * 100 as profit_margin_percentage
from revenue
join costs
on revenue.ride_month_2 = costs.ride_month_2
