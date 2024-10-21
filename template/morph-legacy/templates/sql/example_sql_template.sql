-- Morph SQL configuration
-- For more information: https://www.morphdb.io/docs
{{
	config(
		name="{MORPH_NAME}",
		description="{MORPH_DESCRIPTION}",
        connection_slug="{MORPH_CONNECTION}",
	)
}}

select 1 as test
