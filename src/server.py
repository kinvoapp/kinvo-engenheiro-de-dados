from flask import Flask

import spacy
import json


from scrapy.crawler import CrawlerProcess
import os


import spider.spider as spider

nlp = spacy.load('pt_core_news_sm')
app = Flask(__name__)


@app.route('/')
def home():
    return open('./web/index.html').read().replace("msg",'/minerar para minerar<br>/extrair para extrair')


@app.route('/minerar')
def minerarSalvar():
    return ''

@app.route('/extrair')
def extrairEntidades():
    with open('data/dados.json', 'r', encoding='utf-8') as news_file:
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
