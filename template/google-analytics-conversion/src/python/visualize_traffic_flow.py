import pandas as pd

import morph
from morph import MorphGlobalContext
import plotly.graph_objects as go

# For more information: https://docs.morph-data.io
@morph.func
@morph.variables("target_link", default="PUT_YOUR_DEFAULT_TARGET_LINK")
@morph.load_data("calculate_traffic_flow")
def visualize_traffic_flow(context: MorphGlobalContext):
    # target link
    target_link = context.vars["target_link"]

    # Load data from the previous cell
    traffic_flow_df = context.data["calculate_traffic_flow"]
    page_referrer = traffic_flow_df["page_referrer"].tolist()
    count = traffic_flow_df["count"].values
    nodes = page_referrer
    nodes.append(target_link)

    link_sources = [i for i in range(len(count))]
    link_targets = [len(nodes) - 1 for _ in range(len(count))]

    fig = go.Figure(
        data=[
            go.Sankey(
                valueformat = ".0f",
                valuesuffix = "views",
                # Define nodes
                node = dict(
                    pad = 15,
                    thickness = 15,
                    line = dict(color = "black", width = 0.5),
                    label =  nodes,
                    color = "blue"
                ),
                # Add links
                link = dict(
                    source = link_sources,
                    target = link_targets,
                    value =  count
                )
            )
        ]
    )

    fig.update_layout(
        title_text="GA4 Conversion Traffic Path Analysis",
        font_size=10
    )
    return fig
