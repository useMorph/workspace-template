import os

import boto3
import morph
import pandas as pd
from morph import MorphGlobalContext


# Morph decorators
# The `@morph.func` decorator required to be recognized as a function in morph.
# For more information: https://www.morph-data.io
@morph.func
@morph.variables("start_date", default="2024-07-01")
@morph.variables("end_date", default="2024-07-31")
@morph.variables("product_code", default=None)
def get_aws_cost(context: MorphGlobalContext) -> pd.DataFrame:
    # setup AWS session
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )
    # get client for cost explorer
    ce = session.client("ce")

    start_date = context.vars["start_date"]
    end_date = context.vars["end_date"]
    if "T" in start_date:
        start_date = start_date.split("T")[0]
    if "T" in end_date:
        end_date = end_date.split("T")[0]
    product_code_filter = context.vars["product_code"]
    if product_code_filter == "" or product_code_filter == "all":
        product_code_filter = None

    # get cost report
    response = ce.get_cost_and_usage(
        TimePeriod={"Start": start_date, "End": end_date},
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
        GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}],
    )

    # format cost data
    data = []
    if "ResultsByTime" in response:
        for result_by_time in response["ResultsByTime"]:
            time_period = result_by_time["TimePeriod"]["Start"]
            year = int(time_period.split("-")[0])
            month = int(time_period.split("-")[1])
            for group in result_by_time["Groups"]:
                service = group["Keys"][0]
                amount = float(group["Metrics"]["UnblendedCost"]["Amount"])
                data.append([year, month, service, amount])
    else:
        print("No 'ResultsByTime' found in response")

    result = pd.DataFrame(
        data, columns=["year", "month", "product_code", "unblended_cost"]
    )
    # Convert unblended_cost to float and display up to 2 decimal places
    result["unblended_cost"] = result["unblended_cost"].astype(float).round(2)
    # Filter by specified product_code
    if product_code_filter:
        result = result[result["product_code"] == product_code_filter]
    # Aggregate unblended_cost by usage_start_date and product_code, and return as pd.DataFrame
    result = (
        result.groupby(["product_code", "year", "month"])["unblended_cost"]
        .sum()
        .reset_index()
    )
    # Rename unblended_cost to amount
    result = result.rename(columns={"unblended_cost": "amount"})
    return result
