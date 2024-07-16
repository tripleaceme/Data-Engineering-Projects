-- 3hrs ride at most
with clean_bikes as (
    select * ,timestampdiff('minutes', started_at,ended_at) as total_mins
                        from {{ ref('staging_blue_rides') }}
                        where
                        RIDEABLE_TYPE is not null 
                        and STARTED_AT is not null 
                        and ENDED_AT is not null 
                        and START_STATION_ID is not null 
                        and END_STATION_ID is not null 
                        and MEMBER_CASUAL is not null 
                        and total_mins  <= 180 )

select * from clean_bikes