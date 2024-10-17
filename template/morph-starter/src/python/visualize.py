import morph
import plotly.express as px
from morph import MorphGlobalContext


# Morph decorators
# The `@morph.func` decorator required to be recognized as a function in morph.
# The `@morph.load_data` decorator required to load data from parent file or function.
#   - The parent is executed before the current function and the data is passed to the current function as `context.data``.
# For more information: https://www.morphdb.io/docs
@morph.func(
    name="visualize",
    description="Example Visualization cell",
)
@morph.load_data("calculate_customer_orders")
def main(context: MorphGlobalContext) -> px.bar:
    data = context.data["calculate_customer_orders"]
    fig = px.bar(data, x="customer_id", y="sales")
    fig.update_layout(title="Plotly Plot")
    return fig
