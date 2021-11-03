import requests
from bs4 import BeautifulSoup

class Bot():
    def get_page(self, page):
        url = "https://www.avito.ru/tatarstan/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?f=ASgBAgECAkTGB~pm7gmmZwFFxpoMFXsiZnJvbSI6MSwidG8iOjE1MDAwfQ&p=" + str(page)
        request = requests.get(url)
        return request.text
    def count_pages(self):
        text = self.get_page(1)
        bs = BeautifulSoup(text, "html.parser")
        
        container = bs.select('a.pagination-page')
        print(container)
        last_button = container[-1]
        href = last_button.get('href')
        url = href.rsplit("=", 1)[-1]
        print(url)
        
    def parse(self):
        pages = self.count_pages()
        
   
def main():
    parser = Bot()
    parser.count_pages()
    
main()

# all_urls = []
#all_links = bs.find_all("a", {"itemprop": "url"})

#for link in all_links:
    #all_urls.append("https://www.avito.ru" + link["href"])
