from flask import Flask

import spacy
import json
import requests


nlp = spacy.load('pt_core_news_sm')
app = Flask(__name__)


@app.route('/')
def home():
    return open('./web/index.html').read().replace("msg",'/minerar para minerar<br>/extrair para extrair')


@app.route('/minerar')
def minerarSalvar():
    params = {
        'spider_name': 'finance-news',
        'start_requests': True
    }
    response = requests.get('http://localhost:9080/crawl.json', params)
    data = response.json()

    result = data['items'][:5]

    with open('data/noticias.json', 'w+', encoding='utf-8') as noticias_file:
        json.dump(result, noticias_file, ensure_ascii=False)

    return {'data': result}

@app.route('/extrair')
def extrairEntidades():
    with open('data/noticias.json', 'r', encoding='utf-8') as news_file:
        news = json.loads(news_file.read())[0:5]
    output = {}
    for new in news:
        new = new['news']
        doc = nlp(new)
        entidades = []
        for entity in doc.ents:
            entidades.append({entity.text: entity.label_})
        output[new] = entidades
    return output
