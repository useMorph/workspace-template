import morph
import pandas as pd
from morph import MorphGlobalContext


# Morph decorators
# The `@morph.func` decorator required to be recognized as a function in morph.
# The `@morph.load_data` decorator required to load data from parent file or function.
#   - The parent is executed before the current function and the data is passed to the current function as `context.data``.
# For more information: https://www.morphdb.io/docs
@morph.func(
    name="example_python_cell",
    description="Example Python cell",
)
@morph.load_data("example_sql_cell")
def main(context: MorphGlobalContext) -> pd.DataFrame:
    # Load data from the previous cell
    sql_result_df = context.data["example_sql_cell"]
    return sql_result_df
