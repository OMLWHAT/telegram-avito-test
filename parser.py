import urllib.parse

import requests
from bs4 import BeautifulSoup

urls = []

class AvitoParser:
    def get_page(self):
        url = "https://www.avito.ru/tatarstan/bytovaya_elektronika?f=ASgCAgECAUXGmgwVeyJmcm9tIjoxLCJ0byI6MTUwMDB9&q=Видеокарты"
        request = requests.get(url)
        bs = BeautifulSoup(request.text, "html.parser")
    
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
            urls.append(block)

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
