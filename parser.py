import requests
from bs4 import BeautifulSoup

url = "https://www.avito.ru/tatarstan/bytovaya_elektronika?f=ASgCAgECAUXGmgwVeyJmcm9tIjoxLCJ0byI6MTUwMDB9&q=Видеокарты"
request = requests.get(url)
bs = BeautifulSoup(request.text, "html.parser")

all_urls = []
all_links = bs.find_all("a", {"data-marker": "title"})

for link in all_links:
    all_urls.append("https://www.avito.ru" + link["href"])
print(all_urls)
