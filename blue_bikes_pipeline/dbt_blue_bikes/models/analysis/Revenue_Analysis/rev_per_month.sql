
with ride as (
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
        avg(timestampdiff('minutes', started_at,ended_at)) as avg_duration_minutes,
        sum(case when member_casual = 'member' then 1 else 0 end) as total_revenue
    from {{ ref('insight_data') }}
    group by 1,2
)

select
ride_month_2,
    
    ride_count,
    avg_duration_minutes,
    total_revenue
from ride
order by ride_month asc