import os

import pandas as pd
import pytest
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient
from blob_io.blob_io import read_csv, write_csv


@pytest.fixture()
def test_data():
    data = {
        "A": [1, 2, 3],
        "B": ["A", "B", "C"]
    }
    return pd.DataFrame(data=data)   
    
def test_read_write(test_data):
    _setup_container()
    path = "test/test.csv"
    write_csv(test_data, path, index=False)
    df = read_csv(path)
    pd.testing.assert_frame_equal(test_data, df)

def _setup_container(name: str = "test"):
    connect_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    try:
        blob_service_client.create_container(name)
    except ResourceExistsError:
        pass
