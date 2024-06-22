with orders_source as (
      select * from {{ source('sales', 'orders') }}
)

select * from orders_source