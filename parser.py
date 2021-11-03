import requests
from bs4 import BeautifulSoup

total_urls = []

class Bot():
    def get_page(self, page):
        url = f"https://www.avito.ru/tatarstan/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?f=ASgBAgECAkTGB~pm7gmmZwFFxpoMFXsiZnJvbSI6MSwidG8iOjE1MDAwfQ&p={page}"
        request = requests.get(url)
        
        return request.text
    
    def get_ads(self, pages):
        text = self.get_page(pages)
        bs = BeautifulSoup(text, "html.parser")
        
        urls = []
        ads = bs.find_all("a", {"itemprop": "url"})
        
        for ad in ads:
            urls.append("https://www.avito.ru" + ad["href"])
            
        return urls
        
        
    def count_pages(self):
        text = self.get_page(1)
        bs = BeautifulSoup(text, "html.parser")
        
        container = bs.select('a.pagination-page')
        last_button = container[-1]
        url = last_button.get('href')
        pages = href.rsplit("=", 1)[-1]
        
        return pages
        
    def parse(self):
        pages = self.count_pages()
        
        for block in range(1, pages + 1):
            blocks = self.get_ads(block)
            total_urls.append(blocks)
            
        
   
def main():
    parser = Bot()
    parser.count_pages()
    
if __name__ == '__main__':
    main()
