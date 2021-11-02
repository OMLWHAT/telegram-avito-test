import requests
from bs4 import BeautifulSoup

url = "https://www.avito.ru/naberezhnye_chelny/nedvizhimost"
request = requests.get(url)
bs = BeautifulSoup(request.text, "html.parser")

all_links = bs.find_all("a", {"class": "link-link-MbQDP"})

for links in all_links:
    print("https://www.avito.ru" + links["href"])
