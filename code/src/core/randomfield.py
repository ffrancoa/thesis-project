import os

import numpy as np
import pandas as pd

DEFAULT_ERROR_VALUE = -8888

def read_dataset(df_relative_path: str, error_value_indicator: float = DEFAULT_ERROR_VALUE):
    df_global_path = os.path.join(os.getcwd(), df_relative_path)

    try:
        df = pd.read_csv(df_global_path)
    except FileNotFoundError:
        print(f"error: file '{df_relative_path}' does not exist")
        return None
    else:
        cleaned_df = clean_dataset(df, error_value_indicator)
        return cleaned_df

def clean_dataset(raw_df: pd.DataFrame, error_value_indicator: float):
    return raw_df.replace(error_value_indicator, np.nan)
