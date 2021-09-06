from flask import Flask

import spacy
import json
import requests
import os.path

nlp = spacy.load('pt_core_news_sm')
app = Flask(__name__)


@app.route('/')
def home():
    return {'mensage': 'Para minerar /mining, para extrair entidades /extract-entities'}


@app.route('/mining')
def mining():
    response = requests.get('http://localhost:9080/crawl.json', {
        'spider_name': 'finance-news',
        'start_requests': True
    })

    result = response.json()['items']

    response = requests.get('http://localhost:9080/crawl.json', {
        'spider_name': 'ultimo-instante',
        'start_requests': True
    })

    result.extend(response.json()['items'])
    data = {'result': result}
    with open('data/news.json', 'w+', encoding='utf-8') as new_file:
        json.dump(data, new_file, ensure_ascii=False)

    return data


@app.route('/extract-entities')
def extractEntities():
    if not(os.path.exists('data/news.json')):
        return {'mensage': 'realize a mineração dos dados primeiro'}

    with open('data/news.json', 'r', encoding='utf-8') as news_file:
        news = json.loads(news_file.read())

    result = []
    for new in news['result']:
        doc = nlp(new['description'])
        entities = []
        for entity in doc.ents:
            entities.append({'text': entity.text, 'label': entity.label_})
        result.append({'description': new['description'], 'entities': entities})
    return {'result': result}
