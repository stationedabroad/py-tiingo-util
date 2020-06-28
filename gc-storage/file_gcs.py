from io import BytesIO
from gcloud import storage
from typing import Iterable
from file_abc import FileRepoABC

class GCSFileRepo(FileRepoABC):
    def __init__(self, credentials_path: str, bucket_name: str) -> None:
        self.bucket_name = bucket_name
        self._client = storage.Client.from_service_account_json(json_credentials_path=credentials_path)
        self.bucket = self._client.get_bucket(self.bucket_name)

    def get_files(self, path: str) -> Iterable[BytesIO]:
        for blob in self.bucket.list_blobs():
            with BytesIO() as bytesio:
                blob.download_to_file(bytesio)
                yield bytesio