from hashlib import md5
from io import BytesIO
from typing import List
from file_abc import FileRepoABC

class FileProcessor:
    def __init__(self, repo: FileRepoABC, path: str = None) -> None:
        self.resource_path = path
        self.repo = repo

    def __len__(self) -> int:
        return sum([1 for _ in self.repo.get_files(self.resource_path)])  

    def run(self) -> List[str]:
        return [self.process_file(file) for file in self.repo.get_files(self.resource_path)]

    def process_file(self, f: BytesIO) -> str:
        return md5(f.getvalue()).hexdigest()
