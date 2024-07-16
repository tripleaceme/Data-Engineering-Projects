with raw_bike_data as(
                        select * 
                        from {{ source('bikes', 'rides') }}
)
select * from raw_bike_data