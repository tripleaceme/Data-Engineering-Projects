with station_count as (

    select municipality, count(station_id) as total_stations, sum(total_docks) as total_docks
    from {{ ref('staging_blue_stations') }}
    group by 1
)
select * from station_count