select country, count(country) total_appearance_without_cat
from {{ ref('wines_without_category') }}
group by country
order by count(country) desc
limit 10