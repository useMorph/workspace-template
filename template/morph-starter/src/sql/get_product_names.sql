-- Morph SQL configuration
-- For more information: https://www.morph-data.io
{{
	config(
		name="get_product_names"
	)
}}

select
	distinct product_name
from
	customer_orders
