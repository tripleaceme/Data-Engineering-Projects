with insight_data as (
                select *,
                case when hour(right(started_at, 12)::time) between 0 and 11 then 'AM'
                else 'PM' end as start_time_of_ride,
                
                case when hour(right(ended_at, 12)::time) between 0 and 11 then 'AM'
                else 'PM' end as end_time_of_ride,
                
                -- Pricing category data gotten from the website:: https://bluebikes.com/pricing
                case when member_casual = 'casual' and total_mins <= 30 then 'Single Ride'
                     when member_casual = 'casual' and total_mins > 30 then 'Day Pass'
                     when member_casual = 'member' and total_mins <= 45 then 'Monthly/Annual'
                     when member_casual = 'member' and total_mins > 45 then 'Income Eligible'
                else  'Bad Ride' end as category,
                -- Pricing value data gotten from the website:: https://bluebikes.com/pricing
                case when category = 'Single Ride'  then 2.50
                     when category = 'Day Pass'  then 10.00
                     when category = 'Monthly/Annual'  then 20.83 -- Average of the two prices
                     when category = 'Income Eligible'  then 0.00
                end as pricing,

                case when start_time_of_ride != end_time_of_ride 
                     and end_time_of_ride = 'AM' then 'Next Day Ride'
                else 'Same Day Ride' 
                end as ride_option
               from {{ ref('clean_bikes') }} )

select * from insight_data