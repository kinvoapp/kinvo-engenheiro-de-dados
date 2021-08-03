from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    site = requests.get("https://financenews.com.br").text
    soup = BeautifulSoup(site, 'html.parser')
    news = soup.find_all('div', class_="manchete manchete3 light")
    print(soup.title.string)
    print(type(news))
    if news is not None:
        for i in news:
            print(i.text)
        with open('news.csv', 'a', newline='', encoding='UTF-8') as f:
            envio = news

        return render_template('index.html', envio=envio)


if __name__ == "__main__":
    app.run(debug=True)
