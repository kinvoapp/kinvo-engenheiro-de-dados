from flask import Flask, render_template
from requests.api import request
from views import views
import requests
import json
import os.path
app = Flask(__name__, static_folder='static')

#Função para criar dicionários afim de facilitar a API
def createDict(noticia, url, conteudo):
    return {
        "News" : noticia,
        "URL" : url,
        "Conteudo" : conteudo
    }       
#Index
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

#Minerar as notícias
@app.route("/minerar", methods=['GET'])
def scrape():
    return views.mine_and_get()

#Reconhecer as entidades nas notícias mineradas
@app.route("/processar", methods=['GET'])
def nlp():
    return views.nlp_api()  

#Visualizar as entidades reconhecidas
@app.route("/tabelanlp", methods=['GET'])
def front():
    response = requests.get('http://127.0.0.1:5000/processar', headers={"content-type":"application/json;charset=UTF-8"})
    data = response.json()
    return render_template("front.html", data = data)

#Visualizar as notícias mineradas
@app.route("/tabelanews", methods=['GET'])
def tablenews():
    if(os.path.isfile('data.json')):
        all_dicts = []
        with open('data.json', 'r', encoding="utf8") as all_news:
            news = json.load(all_news)
            for noticia in news:
                dict = createDict(noticia['title'], noticia['url'], noticia['conteudo'])
                all_dicts.append(dict)
        return render_template("tablenews.html", data = all_dicts, fileExists = True)  
    response = requests.get('http://127.0.0.1:5000/minerar', headers={"content-type":"application/json;charset=UTF-8"})
    data = response.json()
    return render_template("tablenews.html", data = data, fileExists = False)

#Página 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
if __name__ == '__main__':
    app.run(debug=True) 