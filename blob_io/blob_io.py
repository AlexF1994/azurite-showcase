import pandas as pd

from blob_io.utils import _add_protocol_prefix


def read_csv(blob_path: str, **kwargs) -> pd.DataFrame:
    blob_path_adjusted = _add_protocol_prefix(blob_path)
    return pd.read_csv(blob_path_adjusted, **kwargs)  # type: ignore

def write_csv(df: pd.DataFrame, blob_path: str, **kwargs):
    blob_path_adjusted = _add_protocol_prefix(blob_path)
    df.to_csv(blob_path_adjusted, **kwargs)
