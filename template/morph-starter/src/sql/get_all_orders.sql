-- Morph SQL configuration
-- For more information: https://www.morph-data.io
{{
	config(
		name="get_all_orders"
	)
}}

select
	*
from
	customer_orders
{% if product_name != "all" %}
where
	product_name = '{{ product_name }}'
{% endif %}
