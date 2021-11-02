import requests
from bs4 import BeautifulSoup

url = "https://www.avito.ru/naberezhnye_chelny/nedvizhimost"
request = requests.get(url)
bs = BeautifulSoup(request.text, "html.parser")

all_links = bs.find_all("a", {"data-marker": "title"})

for link in all_links:
    print("https://www.avito.ru" + link["href"])
    
