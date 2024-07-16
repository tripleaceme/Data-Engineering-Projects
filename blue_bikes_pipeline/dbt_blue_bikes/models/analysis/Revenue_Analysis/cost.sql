with cost_data as (
    select
            DECODE(EXTRACT(month FROM started_at),
  1, 'January',
  2, 'February',
  3, 'March',
  4, 'April',
  5, 'May',
  6, 'June',
  7, 'July',
  8, 'August',
  9, 'September',
  10, 'October',
  11, 'November',
  12, 'December') AS ride_month_2,
        extract('month',started_at) as ride_month,
        count(*) as ride_count,
        avg(timestampdiff('minutes', started_at,ended_at)) as avg_duration_minutes
    from {{ ref('insight_data') }}
    group by 1, 2
)

select
    ride_month_2,
    ride_count,
    avg_duration_minutes,
    ride_count * 1 as maintenance_cost,  -- Assuming $1 maintenance cost per ride
    ride_count * 0.5 as other_costs      -- Assuming $0.5 other costs per ride
from cost_data
order by ride_month