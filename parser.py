import requests
from bs4 import BeautifulSoup as bs


class Bot:
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }

    def __init__(self):
        self.get_html()

    def get_html(self):
        url = "https://m.avito.ru/rossiya/nedvizhimost"
        with requests.Session() as session:
            response = session.get(url, headers=self.headers)
        return response.text

    def parse_html(self, html):
        urls = []
        soup = bs(html, 'lxml')
        main__div = soup.find_all('div', {'class': 'ON2y7'})
        sec__div = main__div.find('div', {'class': '_BTUA'})
        thi__div = sec__div.find('div', {'class': '_U2a8'})
        fou__div = thi__div.find('div', {'class': 'xTVII'})
        for data in fou__div :
            try:
                a = data.find('a', {'itemprop': 'url'})['href']
                print(a)
                links = {
                    'href': f'https://m.avito.ru{a}'
                }
                urls.append(links)
            except:
                continue
        return urls


def main():
    bot = Bot()
    html = bot.get_html()
    result = bot.parse_html(html)
    print(result)


if __name__ == '__main__':
    main()
