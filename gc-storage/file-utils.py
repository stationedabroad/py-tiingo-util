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
        self.bucket = self.client.get_bukcet(self.resource_path)

    def run(self):
        pass

    def process_nlob(self):
        pass
