with products_source as (
      select * from {{ source('sales', 'products') }}
)

select * from products_source