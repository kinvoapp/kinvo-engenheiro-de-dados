from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    site = requests.get("https://financenews.com.br").content
    soup = BeautifulSoup(site, 'html.parser')
    news = soup.select("div.manchete.manchete3.light > h3 > a")
    data = []
    for result in news:
        data.append(result.text)
        print(data)
    with open('news.csv', 'a', newline='', encoding='UTF-8') as f:
        return render_template('index.html', list_news=data)


if __name__ == "__main__":
    app.run(debug=True)
