 with top_start as (
    
    select st.station_name, count(*) as total_rides, 'Start Station' as station
    from {{ ref('staging_blue_stations') }}  as st
    join {{ ref('staging_blue_rides') }} as insd 
    on st.station_id = insd.start_station_id
    group by 1 
    limit 20 
),

 top_end as (
    select st.station_name, count(*) as total_rides, 'End Station' as station
    from {{ ref('staging_blue_stations') }} as st
    join {{ ref('staging_blue_rides') }} as insd 
    on st.station_id = insd.end_station_id
    group by 1 
    limit 20
),

final_station as (
select * from top_start 
union
select * from top_end)

select * from final_station
order by station desc, total_rides desc  