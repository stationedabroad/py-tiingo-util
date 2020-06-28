from io import BytesIO
from unittest import main as testmain
from unittest.mock import Mock
from unittest.mock import patch
from unittest import TestCase

from file_processor import FileProcessor
from file_abc import FileRepoABC

class TestFileProcessor(TestCase):
    def test_run_file_hasher(self):
        mock_repo = Mock(spec=FileRepoABC)
        mock_repo.get_files.return_value = [BytesIO(b"foo"), BytesIO(b"bar")]
        fp = FileProcessor(mock_repo, None)
        results = fp.run()
        self.assertEqual(results, ['acbd18db4cc2f85cedef654fccc4a4d8', '37b51d194a7513e45b56f6524f2d51f2'])


if __name__ == '__main__':
    testmain()                