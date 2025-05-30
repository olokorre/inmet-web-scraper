from requests import get
from pathlib import Path
from tqdm import tqdm
from hashlib import md5


class Downloader:
    
    __url: str
    __storage: str
    
    def __init__(self, url: str, storage: str):
        self.__url = url
        self.__storage = storage
        
    def __checkIntegrity(self, file_path: str) -> str:
        return md5(open(file_path, 'rb').read()).hexdigest()
    
    def download(self) -> tuple[str, str]:
        name = self.__url.split('/')[-1]
        print(f"Downloading {name} to {self.__storage}...")
        Path(self.__storage).mkdir(parents=True, exist_ok=True)
        response = get(self.__url, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024
        with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
            with open(self.__storage + '/' + name, "wb") as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
        if total_size != 0 and progress_bar.n != total_size:
            raise RuntimeError("Could not download file")
        return (name, self.__checkIntegrity(self.__storage + '/' + name))

if __name__ == "__main__":
    utl = 'https://portal.inmet.gov.br/uploads/dadoshistoricos/2025.zip'
    storage = 'data/'
    downloader = Downloader(utl, storage)
    (name, integrity) = downloader.download()
    print(f"Downloaded file {name} integrity: {integrity}")
