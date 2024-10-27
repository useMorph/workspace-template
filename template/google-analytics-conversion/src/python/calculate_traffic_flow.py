import pandas as pd

import morph
from morph import MorphGlobalContext
import plotly.graph_objects as go

# For more information: https://docs.morph-data.io
@morph.func
@morph.variables("target_link", default="PUT_YOUR_DEFAULT_TARGET_LINK")
@morph.load_data("ga_data_extraction")
def calculate_traffic_flow(context: MorphGlobalContext) -> pd.DataFrame:
    # target link
    target_link = context.vars["target_link"]

    # Load data from the previous cell
    sql_result_df = context.data["ga_data_extraction"]

    # Filtering rows where page_location is `target_link`
    filtered_df = sql_result_df[sql_result_df["page_location"] == target_link]

    # Grouping by "page_referrer" and "page_location", and counting the occurrences
    grouped_df = filtered_df.groupby(["page_referrer", "page_location"]).size().reset_index(name="count")

    return grouped_df
