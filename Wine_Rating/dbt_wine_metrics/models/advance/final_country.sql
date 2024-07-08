select with_cat.country, total_appearance_cat, total_appearance_without_cat
from {{ ref('top_10_countries_with_cat') }} as with_cat
inner join {{ ref('top_10_countries_without_cat') }} as without_cat
on with_cat.country = without_cat.country
