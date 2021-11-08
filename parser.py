import time
import requests
from itertools import groupby
from bs4 import BeautifulSoup

urls = []

class Bot():
    def get_page(self, page):
        url = f"https://www.avito.ru/tatarstan/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?f=ASgBAgECAkTGB~pm7gmmZwFFxpoMFXsiZnJvbSI6MSwidG8iOjE1MDAwfQ&p={page}&s=104"
        request = requests.get(url)
        
        return request.text
    
    def get_ads(self, pages):
        for page in range(1, pages + 1):
            text = self.get_page(page)
            bs = BeautifulSoup(text, "html.parser")
                               
            ads = bs.find_all("a", {"itemprop": "url"})
           
            for ad in ads:
                urls.append("https://www.avito.ru" + ad["href"])
                        
            return True
        
        
    def count_pages(self):
        text = self.get_page(1)
        bs = BeautifulSoup(text, "html.parser")
        
        buttons = bs.select("a.pagination-page")
        last_button = buttons[-2]
        print(last_button)
        url = last_button.get("href")
        pages = url.rsplit("=", 1)[-1]
        
        print(f"Всего {pages} страниц")
        
        return int(pages)
        
    def parse(self):
        pages = self.count_pages()          
        ads = self.get_ads(pages)
        total_urls = []
        if ads == True:
            total_urls = [el for el, _ in groupby(urls)]
        
        return total_urls
        
   
def main():
    parser = Bot()
    total_urls = parser.parse()
    print(total_urls)
    
if __name__ == "__main__":
    main()
