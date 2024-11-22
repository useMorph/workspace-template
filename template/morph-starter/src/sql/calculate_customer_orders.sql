-- Morph SQL configuration
-- For more information: https://docs.morph-data.io
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
