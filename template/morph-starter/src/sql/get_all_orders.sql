-- Morph SQL configuration
-- For more information: https://www.morphdb.io/docs
{{
	config(
		name="get_all_orders"
	)
}}

select
	*
from
	customer_orders
