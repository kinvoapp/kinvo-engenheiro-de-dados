# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from spacy import load
from scrapy.spiders import XMLFeedSpider
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import json
#python -m spacy download pt_core_news_lg
nlp = load('pt_core_news_lg')
noticias = []
noti = 5


def reestruturar(noticias):
    resposta = []
    for i in range(len(noticias)):
        resposta.append({
            "titulo": str(noticias[i]["titulo"]),
            "link": str(noticias[i]["link"]),
            "conteudo": str(noticias[i]["conteudo"]),
            "entidades": noticias[i]["entidades"]
        })
    return resposta


class ExtrairNoticias(XMLFeedSpider):
    name = 'extrairnoticias'
    allowed_domains = ['financenews.com.br']
    start_urls = ['https://financenews.com.br/feed/']
    iterator = 'xml'
    itertag = 'rss'

    def parse_node(self, response, selector):
        response.selector.register_namespace(
            'content', 'http://purl.org/rss/1.0/modules/content/')
        tree = ET.ElementTree(ET.fromstring(selector.extract()))
        root = tree.getroot()
        ns = {'content': 'http://purl.org/rss/1.0/modules/content/'}
        conteudos = []
        for chanel in root.findall("channel"):
            for child in chanel.findall("item"):
                for title in child.findall("content:encoded", ns):
                    tasdf = BeautifulSoup(
                        title.text, 'html.parser').find_all('p')
                    conteudo = ''
                    for h in tasdf:
                        if h.find_all('span') != []:
                            conteudo = str(conteudo) + \
                                str(h.find('span').text)+"  "
                conteudos.append(conteudo)
        canais = selector.xpath('/rss/channel/item/title/text()').extract()
        links = selector.xpath('/rss/channel/item/link/text()').extract()
        cont = 0
        for i in range(len(selector.xpath('/rss/channel/item').extract())):
            if cont == 5:
                break
            if str(conteudos[i].replace(u'\xa0', u' ')) != '':
                noticias.append({"titulo": str(canais[i].replace(
                    u'\xa0', u' ')), "link": str(links[i]), "conteudo": str(conteudos[i].replace(u'\xa0', u' ')), "entidades": []})
                cont += 1


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(ExtrairNoticias)
process.start()
process.stop()
with open('noticias.json', 'w', encoding='utf8') as json_file:
    json.dump(reestruturar(noticias), json_file, ensure_ascii=False)
with open('noticias.json', 'r', encoding='utf8') as f:
    noticias = json.load(f)

for noticia in noticias:
    for entidade in nlp(noticia['conteudo']).ents:
        noticia['entidades'].append(
            {"entidade": str(entidade.text), "tipo": str(entidade.label_)})


with open('dados.json', 'w', encoding='utf8') as json_file:
    json.dump(
        reestruturar(noticias), json_file, ensure_ascii=False)
with open('dados.json', 'w', encoding='utf8') as json_file:
    json.dump(
        reestruturar(noticias), json_file, ensure_ascii=False)

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False
@app.route("/")
def hello():
    return jsonify(reestruturar(noticias))
app.run(host="127.0.0.1")
