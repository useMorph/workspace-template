{{
    config(
        name = "get_aws_product_list"
    )
}}

select
    distinct product_code
from
    {{load_data("get_aws_cost")}}
