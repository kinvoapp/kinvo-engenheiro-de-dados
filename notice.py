import requests
from bs4 import BeautifulSoup

site = requests.get("https://financenews.com.br").content
# "site" object receives the order content.

soup = BeautifulSoup(site, 'html.parser')
# soup download from the site the html.

news = soup.find_all('div', class_="manchete manchete3 light")


with open('news.csv', 'a', newline='', encoding='UTF-8') as f:
    print(soup.title.string)
    print(news)
