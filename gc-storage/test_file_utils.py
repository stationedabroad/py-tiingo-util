from unittest import main as testmain
from unittest.mock import Mock
from unittest.mock import patch
from unittest import TestCase
from file_utils import FileProcessor

class TestFileProcessor(TestCase):

    def test_run_returns_md5(self):

        with patch('file_utils.storage'):
            fp = FileProcessor('some/bucket')
            with patch.object(fp, 'bucket') as mock_bucket:
                mock_blob = Mock(name='mock_blob')
                def mock_blob_download_to_file(bytez):
                    bytez.write(b'arrangeinserver')
                mock_blob.download_to_file = mock_blob_download_to_file
                mock_bucket.list_blobs.return_value = [mock_blob]
                result = fp.run()
                self.assertEqual(result, ['53a195336dfdd9034b8371408f2d7729'])

if __name__ == '__main__':
    testmain()                
