-- Morph SQL configuration
-- For more information: https://www.morphdb.io/docs
{{
	config(
		name="get_product_names"
	)
}}

select
	distinct product_name
from
	customer_orders
