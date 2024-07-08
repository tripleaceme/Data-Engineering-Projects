select country, count(country) total_appearance_cat
from {{ ref('wines_with_category') }}
group by country
order by count(country) desc
limit 10