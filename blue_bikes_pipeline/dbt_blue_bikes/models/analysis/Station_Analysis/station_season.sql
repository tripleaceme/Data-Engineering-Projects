with station_season_rides as (

select seasonal_status, count(*) as total_rides, 'Season' as type
from {{ ref('insight_data') }} as insd
join {{ ref('staging_blue_stations') }} st
on st.station_id = insd.start_station_id and st.station_id = insd.end_station_id
group by 1

),

station_municipality as (

select municipality, count(*) as total_rides, 'Municipality' as type
from {{ ref('insight_data') }} as insd
join {{ ref('staging_blue_stations') }} st
on st.station_id = insd.start_station_id and st.station_id = insd.end_station_id
group by 1

),

final_data as (
    select * from station_season_rides
    union 
    select * from station_municipality 
)

select * from final_data
