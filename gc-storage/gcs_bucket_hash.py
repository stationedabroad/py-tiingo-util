import os
from file_processor import FileProcessor
from file_gcs import GCSFileRepo

APP_PROJECT = os.getenv("GCLOUD_PROJECT")
APP_CREDENTIALS_JSON = os.getenv("GCLOUD_STORAGE_CRED")
COVID_BUCKET = "covid19-datafiles"

def main():
    """ 
        Use custom file processor to pull bcket hashes
    """
    gcs_repo = GCSFileRepo(APP_CREDENTIALS_JSON, COVID_BUCKET)
    fp = FileProcessor(gcs_repo, None)
    gcs_bucket_hashes = fp.run()
    print(gcs_bucket_hashes)

if __name__ == '__main__':
    main()
