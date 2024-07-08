with wine_source as (
    select * from {{ source('raw-wine', 'df_wines') }}
)

select 
"Name" as name, "Country" as country, "Region" as region, 
"Winery" as brand, "Rating" as rating, "NumberOfRatings" as total_ratings , 
"Price" as price, "Year" as year, "Color" as color, "Variety" as category
 from wine_source 
 where  "NumberOfRatings" is not null