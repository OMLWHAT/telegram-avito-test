import urllib.parse

import requests
from bs4 import BeautifulSoup

urls = []

class AvitoParser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15",
            "Accept-Language": "ru",
        }

    def get_page(self, page: int = None):
        params = {
            "radius": 0,
            "user": 1,
        }
        if page and page > 1:
            params["p"] = page

        url = "https://www.avito.ru/tatarstan/bytovaya_elektronika?f=ASgCAgECAUXGmgwVeyJmcm9tIjoxLCJ0byI6MTUwMDB9&q=Видеокарты"
        r = self.session.get(url, params=params)
        return r.text
    
    def get_pagination_limit(self):
        text = self.get_page()
        bs = BeautifulSoup(text, "lxml")

        container = bs.select("a.pagination-page")
        last_button = container[-1]
        href = last_button.get("href")
        if not href:
            return 1
        
        r = urllib.parse.urlparse(href)
        params = urllib.parse.parse_qs(r.query)
        
        return int(params["p"][0])

    def get_blocks(self, page: int = None):
        text = self.get_page(page=page)
        bs = BeautifulSoup(text, "lxml")

        container = bs.select("div.item.item_table.clearfix.js-catalog-item-enum.item-with-contact.js-item-extended")
        
        for item in container:
            block = self.parse_block(item=item)
            print(block)

    def parse_all(self):
        limit = self.get_pagination_limit()

        for i in range(1, limit + 1):
            self.get_blocks(page=i)
            
def main():
    p = AvitoParser()
    p.parse_all()
    print(urls)

if __name__ == "__main__":
    main()
