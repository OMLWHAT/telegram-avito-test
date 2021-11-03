import requests
from bs4 import BeautifulSoup

total_urls = []

class Bot():
    def get_page(self, page):
        url = f"https://www.avito.ru/tatarstan/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?f=ASgBAgECAkTGB~pm7gmmZwFFxpoMFXsiZnJvbSI6MSwidG8iOjE1MDAwfQ&p={page}"
        request = requests.get(url)
        
        return request.text
    
    def get_ads(self, page):
        text = self.get_page(page)
        bs = BeautifulSoup(text, "html.parser")
        
        urls = []
        ads = bs.find_all("a", {"itemprop": "url"})
        
        for ad in ads:
            urls.append("https://www.avito.ru" + ad["href"])
            
        return urls
        
        
    def count_pages(self):
        text = self.get_page(1)
        print(text)
        bs = BeautifulSoup(text, "html.parser")
        
        container = bs.select('a.pagination-page')
        last_button = container[-1]
        url = last_button.get('href')
        print(url)
        pages = url.rsplit("=", 1)[-1]
        
        print(pages)
        
        return len(pages)
        
    def parse(self):
        pages = self.count_pages()
        
        for page in range(1, pages + 1):
            ads = self.get_ads(page)
            total_urls.append(ads)
            
        
   
def main():
    parser = Bot()
    parser.parse()
    
if __name__ == '__main__':
    main()
