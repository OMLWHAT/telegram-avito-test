import requests
from bs4 import BeautifulSoup

fake_urls = []
total_urls = []

class Bot():   
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'Accept-Language': 'ru'
    }
    
    def __init__(self):
        self.get_page()
    
    def get_page(self, page=None):
        url = f"https://www.avito.ru/tatarstan/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?f=ASgBAgECAkTGB~pm7gmmZwFFxpoMFXsiZnJvbSI6MSwidG8iOjE1MDAwfQ&p={page}"
        with requests.Session() as session:
            response = session.get(url, headers=self.headers)
        
        return response.text
    
    def get_ads(self, pages):
        urls = []
        for page in range(1, pages + 1):
            print(page)
            text = self.get_page(page=page)
            bs = BeautifulSoup(text, "html.parser")
            
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
        pages = url.rsplit("=", 1)[-1]
        
        return len(pages)
        
    def parse(self):
        pages = self.count_pages()          
        ads = self.get_ads(pages)
        fake_urls.append(ads)
        total_urls.append(fake_urls[1])  
        
   
def main():
    parser = Bot()
    parser.parse()
    print(total_urls)
    
if __name__ == '__main__':
    main()
