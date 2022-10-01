import pandas as pd
import pytest

from blob_io.blob_io import read_csv, write_csv


@pytest.fixture()
def test_data():
    data = {
        "A": [1, 2, 3],
        "B": ["A", "B", "C"]
    }
    return pd.DataFrame(data=data)   
    
def test_read_write(test_data):
    path = "test/test.csv"
    write_csv(test_data, path, index=False)
    df = read_csv(path)
    pd.testing.assert_frame_equal(test_data, df)
