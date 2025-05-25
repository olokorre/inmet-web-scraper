from source.downloader import Downloader
from source.scraper import Scraper


scraper = Scraper('https://portal.inmet.gov.br/dadoshistoricos')
urls = scraper.extractUrls()

if __name__ == "__main__":
    storage = 'data/'
    for url in urls:
        downloader = Downloader(url, storage)
        downloader.download()
