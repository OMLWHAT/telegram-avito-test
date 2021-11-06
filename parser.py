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
            ads_body = bs.find_all("div", {"class": "iva-item-body-R_Q9c"})
            for ads in ads_body:
                ads_title = ads.find("div", {"class": "iva-item-titleStep-_CxvN"})
                for ad in ads_title:
                    dates = ads.find("div", {"data-marker": "item-date"})
                    print(dates.text.split(" ")[1])
                    if dates.text.split(" ")[1] == "секунду":
                        urls.append("https://www.avito.ru" + ad["href"])
                    elif dates.text.split(" ")[1] == "секунд":
                        urls.append("https://www.avito.ru" + ad["href"])
                    elif dates.text.split(" ")[1] == "минуту":
                        urls.append("https://www.avito.ru" + ad["href"])
                    elif dates.text.split(" ")[1] == "минут":
                        urls.append("https://www.avito.ru" + ad["href"])    
                    elif dates.text.split(" ")[1] == "час":
                        urls.append("https://www.avito.ru" + ad["href"])    
                    elif dates.text.split(" ")[1] == "часов":
                        urls.append("https://www.avito.ru" + ad["href"])
                    
            #for ad in ads:
                #dates = bs.find_all("div", {"data-marker": "item-date"})
                #for date in dates:
                    #if date.text.split(" ")[1] == "часов": #or date.text.split(" ")[1] == "часов":
                        #urls.append("https://www.avito.ru" + ad["href"])
                        
            return True
        
        
    def count_pages(self):
        text = self.get_page(1)
        bs = BeautifulSoup(text, "html.parser")
        
        buttons = bs.select("a.pagination-page")
        last_button = buttons[-1]
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
