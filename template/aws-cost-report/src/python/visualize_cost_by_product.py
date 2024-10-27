import pandas as pd
import plotly.express as px

import morph
from morph import MorphGlobalContext

@morph.func
@morph.load_data("get_aws_cost")
def visualize_cost_by_product(context: MorphGlobalContext):
    data = context.data["get_aws_cost"]
    # Combine year and month columns to create a date column
    data["date"] = pd.to_datetime(data["year"].astype(str) + "-" + data["month"].astype(str) + "-01")
    # Change the date column to date format
    data["date"] = data["date"].dt.date

    # Calculate total cost per product
    total_cost_per_product = data.groupby("product_code")["amount"].sum().reset_index()

    # Sort in descending order of cost
    total_cost_per_product = total_cost_per_product.sort_values(by="amount", ascending=False)

    # Set categories in sorted order
    data["product_code"] = pd.Categorical(data["product_code"], categories=total_cost_per_product["product_code"], ordered=True)

    fig = px.bar(data, x="date", y="amount", color="product_code", barmode="stack")
    fig.update_layout(title="AWS Cost Trend", xaxis_tickformat="%Y-%m")
    return fig