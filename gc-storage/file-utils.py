from io import BytesIO
from hashlib import md5
from gcloud import storage
from pathlib import Path

# to use credentials drop gc-cloud service accoutn creds into the filder hich this __file__ resides in
print(__file__)
print(Path(__file__).parent.resolve())