import flask
from flask import jsonify
import scrapy
from scrapy.selector import Selector
from scrapy.http import XmlResponse
import requests

#importando funções crawler
from crawler import getNewsFinance, getNewsInstante, homeHeader
from entityGetter import getEntity

app = flask.Flask(__name__)
app.config["DEBUG"] = True
#para ler utf-8
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def home():
    return """<h1>API Notícias</h1>
    <p>Essa API retorna noticias sobre a B3 e entidades</p>
    <h3>Documentação:</h3>
    <p>Sites disponíveis:</p>
    <ul>
    <li>Finance News: "finance"</li>
    <li>Ultimo Instante: "instante"</li>
    </ul>
    <p>End Points:<p>
    <ul>
    <li>"/website": Info sobre o RSS</li>
    <li>"/website/news": Lista de noticias sobre a B3</li>
    <li>"/website/news/entities": Entidades das noticias</li>
    </ul>
    <p>Exemplo:</p>
    <ul>
    <li>/finance/news
    <p>
    {
    "fonte": "https://financenews.com.br", 
    "id": 1, 
    "title": "São Martinho vai pagar dividendos"
  }...</p>
    </li>

    <li>/finance/news/entities
    <p>

    {"id": 1, 
    <br> 
    "title": "São Martinho vai pagar dividendos",
    <br> 
    "entidades": [
              "entidade": "B3", 
              "tipo": "ORG"
      },
      <br> 
      {
              "entidade": "Porto Seguro", 
              "tipo": "LOC"
      } 
      <br> 
    ]
  }...</p>
    </li>

    </ul>
    """



@app.route('/instante', methods=['GET'])
def Instante():
    content = homeHeader('https://www.ultimoinstante.com.br/feed/')
    return jsonify(content)



@app.route('/instante/news', methods=['GET'])
def instanteNews():
    content = getNewsInstante('https://www.ultimoinstante.com.br/feed/')
    return jsonify(content)



@app.route('/instante/news/entities', methods=['GET'])
def entitiesInstante():
    content = getEntity('Instante')
    return jsonify(content)





@app.route('/finance', methods=['GET'])
def Finance():
    content = homeHeader('https://financenews.com.br/feed/')
    return jsonify(content)

@app.route('/finance/news', methods=['GET'])
def financeNews():
    content = getNewsFinance('https://financenews.com.br/feed/')
    return jsonify(content)

@app.route('/finance/news/entities', methods=['GET'])
def entitiesFinance():
    content = getEntity('Finance')
    return jsonify(content)

app.run()