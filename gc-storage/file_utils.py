import os
from io import BytesIO
from hashlib import md5
from gcloud import storage
from pathlib import Path

# to use credentials drop gc-cloud service accoutn creds into the filder hich this __file__ resides in
APP_PROJECT = os.getenv("GCLOUD_PROJECT")
APP_CREDENTIALS_JSON = os.getenv("GCLOUD_STORAGE_CRED")

my_resource_bucket = "covid19-datafiles"


class FileProcessor:
    def __init__(self, resource_path):
        self.resource_path = resource_path
        self.client = storage.Client.from_service_account_json(json_credentials_path=APP_CREDENTIALS_JSON, project=APP_PROJECT) 
        self.bucket = self.client.get_bucket(self.resource_path)

    def __len__(self):
        return sum([1 for _ in self.bucket.list_blobs()])   

    def run(self):
        return [self.process_blob(blob) for blob in self.bucket.list_blobs()]

    def process_blob(self, blob):
        with BytesIO() as blob_contents:
            blob.download_to_file(blob_contents)
            return md5(blob_contents.getvalue()).hexdigest()
