import os

try: 
    github = os.environ["HOST"]
except KeyError:
    github = False

host = github if github else "azurite"
connect_str = f"DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://{host}:10000/devstoreaccount1;"
os.environ["AZURE_STORAGE_CONNECTION_STRING"] = connect_str
    