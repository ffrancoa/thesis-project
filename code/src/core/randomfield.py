from pathlib import Path

import numpy as np
import pandas as pd

DEFAULT_ERROR_VALUE = -8888.0


def load_dataset(
    df_relative_path: str,
    error_value_indicator: float = DEFAULT_ERROR_VALUE
) -> pd.DataFrame:
    
    df_path = Path(df_relative_path).resolve()

    if not df_path.exists():
        raise FileNotFoundError(f"Dataset not found: '{df_relative_path}'")

    df = pd.read_csv(df_path)
    
    return replace_error_values(df, error_value_indicator)


def replace_error_values(
    df: pd.DataFrame,
    error_value_indicator: float
) -> pd.DataFrame:
    
    return df.replace(error_value_indicator, np.nan)
