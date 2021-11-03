import requests
from bs4 import BeautifulSoup

fake_urls = []
total_urls = []

class Bot():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    
    def __init__(self):
        self.get_html()
    
    def get_page(self, page):
        url = f"https://www.avito.ru/tatarstan/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?f=ASgBAgECAkTGB~pm7gmmZwFFxpoMFXsiZnJvbSI6MSwidG8iOjE1MDAwfQ&p={page}"
        with requests.Session() as session:
            response = session.get(url, headers=self.headers)
        
        return request.text
    
    def get_ads(self, pages):
        urls = []
        for page in range(1, pages + 1):
            text = self.get_page(page)
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
