import morph
import pandas as pd
from morph import MorphGlobalContext


# Morph decorators
# The `@morph.func` decorator required to be recognized as a function in morph.
# For more information: https://www.morphdb.io/docs
@morph.func(
    name="{MORPH_NAME}",
    description="{MORPH_DESCRIPTION}",
)
def main(context: MorphGlobalContext) -> pd.DataFrame:
    return pd.DataFrame({{"key1": [1, 2, 3], "key2": [3, 4, 5]}})
