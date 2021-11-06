import time
import requests
from itertools import groupby
from bs4 import BeautifulSoup

urls = []

class Bot():
    def get_ads_page(self, url):
        request = requests.get(url)
        
        return request.text
    
    def get_page(self, page):
        url = f"https://www.avito.ru/tatarstan/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?f=ASgBAgECAkTGB~pm7gmmZwFFxpoMFXsiZnJvbSI6MSwidG8iOjE1MDAwfQ&p={page}"
        request = requests.get(url)
        
        return request.text
    
    def get_ads(self, pages):
        for page in range(1, pages + 1):
            text = self.get_page(page)
            bs = BeautifulSoup(text, "html.parser")
                               
            ads = bs.find_all("a", {"itemprop": "url"})
           
            for ad in ads:
                url = "https://www.avito.ru" + ad["href"]
                ad_text = self.get_ads_page(url)
                ad_bs = BeautifulSoup(ad_text, "html.parser")
                
                ad_page = ad_bs.find("div", {"class": "title-info-metadata-item-redesign"})
                
                print(ad_page)
                
                if ad_page.text.split(" ")[0] == "Сегодня":
                    urls.append(url)
                        
            return True
        
        
    def count_pages(self):
        text = self.get_page(1)
        bs = BeautifulSoup(text, "html.parser")
        
        buttons = bs.select("a.pagination-page")
        last_button = buttons[-1]
        url = last_button.get("href")
        pages = url.rsplit("=", 1)[-1]
        
        print(f"Всего: {pages} страниц")
        
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
