from re import findall
from requests import get

class Scraper:
    
    __baseUrl: str
    
    def __init__(self, baseUrl: str):
        self.__baseUrl = baseUrl
    
    def extractUrls(self) -> list[str]:
        resposta = get(self.__urlBase)
        resposta.raise_for_status()
        padrao = r'href="(https://portal\.inmet\.gov\.br/uploads/dadoshistoricos/\d{4}\.zip)"'
        urls = findall(padrao, resposta.text)
        return urls

if __name__ == "__main__":
    scraper = Scraper("https://portal.inmet.gov.br/dadoshistoricos")
    urls = scraper.extractUrls()
    for url in urls:
        print(url)
