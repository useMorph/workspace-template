import morph
import pandas as pd
from morph import MorphGlobalContext


# Morph decorators
# The `@morph.func` decorator required to be recognized as a function in morph.
# For more information: https://www.morph-data.io
@morph.func(
    name="{PUT_NAME_HERE}",
    description="{PUT_DESCRIPTION_HERE}",
)
def main(context: MorphGlobalContext) -> pd.DataFrame:
    return pd.DataFrame({{"key1": [1, 2, 3], "key2": [3, 4, 5]}})
