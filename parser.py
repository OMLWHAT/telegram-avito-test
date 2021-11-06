import time
import requests
from itertools import groupby
from bs4 import BeautifulSoup

urls = []

class Bot():   
    def get_page(self, page):
        url = f"https://www.avito.ru/tatarstan/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?f=ASgBAgECAkTGB~pm7gmmZwFFxpoMFXsiZnJvbSI6MSwidG8iOjE1MDAwfQ&p={page}"
        request = requests.get(url)
        
        return request.text
    
    def get_ads(self, pages):
        for page in range(1, pages + 1):
            text = self.get_page(page)
            bs = BeautifulSoup(text, "html.parser")
            
            #ads = bs.find_all("a", {"itemprop": "url"})
            dates = bs.find_all("div", {"data-marker": "item-date"})
            for date in dates:
                print(date.text)
                if date.text.rsplit(" ", 1)[1] == "час":
                    print("yes")
            #for ad in ads:
                #urls.append("https://www.avito.ru" + ad["href"])
        
        return True
        
        
    def count_pages(self):
        text = self.get_page(1)
        bs = BeautifulSoup(text, "html.parser")
        
        container = bs.select("a.pagination-page")
        last_button = container[-1]
        url = last_button.get("href")
        pages = url.rsplit("=", 1)[-1]
        
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
