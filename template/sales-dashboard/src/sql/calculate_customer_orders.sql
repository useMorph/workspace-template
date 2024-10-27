-- Morph SQL configuration
-- For more information: https://www.morphdb.io/docs
{{
	config(
		name="calculate_customer_orders"
	)
}}

select
	product_name,
	sum(quantity * unit_price) as sales
from
	customer_orders
group by
	product_name
