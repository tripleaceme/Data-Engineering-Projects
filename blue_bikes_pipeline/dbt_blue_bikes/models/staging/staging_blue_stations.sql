with stations_data as (
 select 
  *
 from {{ source('bikes', 'stations') }}
)
select * from stations_data