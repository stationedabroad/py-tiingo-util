import os
from io import BytesIO
from hashlib import md5
from gcloud import storage
from pathlib import Path

APP_PROJECT = os.getenv("GCLOUD_PROJECT")
APP_CREDENTIALS_JSON = os.getenv("GCLOUD_STORAGE_CRED")

# to use credentials drop gc-cloud service accoutn creds into the filder hich this __file__ resides in
print(f"Running ... {Path(__file__).parent.resolve() / __file__}")
print(APP_CREDENTIALS_JSON, APP_PROJECT)

client = storage.Client.from_service_account_json(json_credentials_path=APP_CREDENTIALS_JSON, project=APP_PROJECT) 
bucket = client.get_bucket("covid19-datafiles")
for blob in bucket.list_blobs():
    print(dir(blob))
    print(blob.md5_hash)
    print(blob.name)
    break