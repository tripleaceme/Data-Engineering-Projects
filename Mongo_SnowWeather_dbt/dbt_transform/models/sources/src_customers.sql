with customer_source as (
      select * from {{ source('sales', 'customers') }}
)

select * from customer_source