from source.database import Database
from source.downloader import Downloader
from source.scraper import Scraper


scraper = Scraper('https://portal.inmet.gov.br/dadoshistoricos')
urls = scraper.extractUrls()
database = Database('index.db')

database.execute('CREATE TABLE IF NOT EXISTS files (url TEXT NOT NULL, file_path TEXT NOT NULL, integrity TEXT, download_data DATETIME NOT NULL, PRIMARY KEY (url))')

if __name__ == "__main__":
    storage = 'data/'
    for url in urls:
        downloader = Downloader(url, storage)
        (file, integrity) = downloader.download()
        database.execute('INSERT INTO files (url, file_path, integrity, download_data) VALUES (?, ?, ?, datetime("now"))', (url, file, integrity))
        print(f'Downloaded: {file} from {url} with integrity {integrity}')
