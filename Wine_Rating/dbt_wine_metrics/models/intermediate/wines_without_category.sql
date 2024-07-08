with wine_category as (
select * 
from
 {{ ref('src_wines') }}
 )
select * from
wine_category
where category = 'Unknown' and  total_ratings is not null  -- 7485 rows 