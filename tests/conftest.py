import os

from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient

connect_str = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://azurite:10000/devstoreaccount1;"
os.environ["AZURE_STORAGE_CONNECTION_STRING"] = connect_str
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
try:
    blob_service_client.create_container("test")
except ResourceExistsError:
    pass
