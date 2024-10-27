import morph
import plotly.express as px
from morph import MorphGlobalContext


@morph.func
@morph.load_data("calculate_customer_orders")
@morph.variables("min_sales", default=10000)
def visualize(context: MorphGlobalContext):
    data = context.data["calculate_customer_orders"]
    min_sales = int(context.vars["min_sales"])

    # Filter data to include only sales greater than or equal to min_sales
    data = data[data["sales"] >= min_sales]

    fig = px.bar(data, x="product_name", y="sales")
    fig.update_layout(xaxis_title='Product Name', yaxis_title='Sales')
    return fig