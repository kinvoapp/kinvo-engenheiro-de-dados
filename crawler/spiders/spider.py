import scrapy
import json
from ..items import NewsItem
from scrapy.exceptions import CloseSpider
#Crio uma lista com palavras provavéis de estarem em notícias sobre ações
key_words_acao = ['desvalorizar', 'dividendos', 'alta', 'baixa', 'ação', 'ações', 'papéis', 'abriu', 'fechou', 'acionista', 'cotação', 'tendência', 'analistas', 'subia', 'descia']
#Abro um arquivo contendo os códigos e nomes das empresas na B3
with open('cod_b3.json', 'r') as empresas_info:
    empresas = json.load(empresas_info)
#Função para verificar se dentro da notícia existe a combinação de nome de empresa + keyword ou código da ação + keyword
def matchNews(news, dict_list = empresas):
    cod_empresas = []
    nome_empresas = []
    
    for itens in dict_list:
        cod_empresas.append(itens['Codigo'])
        nome_empresas.append(itens['Empresa'])

    for cods in cod_empresas:
        if cods in news:
            for key_word in key_words_acao:
                if key_word in news.lower():
                    return True
    
    for nomes in nome_empresas:
        if nomes in news:
            for key_word in key_words_acao:
                if key_word in news.lower():
                    return True
    return False

class newsSpider(scrapy.Spider):
    
    name = 'news'
    allowed_domains = ['financenews.com.br']
    start_urls = ['https://financenews.com.br/category/nao-deixe-de-ler/']
    base_url = 'https://financenews.com.br/'
    newsCounter = 0
    first_time = True
    match_counter = 0
    noticias_corporativas = 0
    def parse(self, response):
        if self.first_time:
            self.first_time = False
            mais_lidas = response.xpath('.//div[@class="lista"]/ul[@class="wpp-list"]/div')
            for news in mais_lidas:
                newsURL = news.xpath('.//h3/a/@href').get()
                if 'noticias-corporativas' in newsURL:
                    continue
                yield scrapy.Request(newsURL, callback=self.parse_news)
            yield scrapy.Request(self.start_urls[0], callback=self.parse)
        else:                
            artigos = response.xpath('.//div[@class="archive-item"]')
            
            for news in artigos:
                firstDiv = news.xpath('.//div[@class="row"]')
                titleDIV = firstDiv.css('div:nth-child(2)')
                newsURL = titleDIV.xpath('.//h2/a/@href').get()
                if 'noticias-corporativas' in newsURL:
                    self.noticias_corporativas += 1
                if self.noticias_corporativas > 1:
                    continue
                print(newsURL)
                yield scrapy.Request(newsURL, callback=self.parse_news)
            prox_pagina = response.xpath(".//a[@class='nextpostslink']/@href").get()
            yield scrapy.Request(prox_pagina, callback=self.parse)
    def parse_news(self,response):
        self.match_counter = 0
        if self.newsCounter >= 5:
            raise CloseSpider('News counter atingido.')
        strConteudo = ''
        title = response.xpath(".//div[@class='title-single']/h1/text()").get()
        contentDIV = response.xpath(".//div[@class='page-post']")
        content = contentDIV.css("p > span::text").getall()
        contentP = contentDIV.css("p::text").getall()
        for paragrafos in content:
            if matchNews(paragrafos):
                self.match_counter += 1
            controlUnicode = ''
            if u'\xa0' in paragrafos:
                controlUnicode = paragrafos.replace(u'\xa0', u'')
            if controlUnicode:
                strConteudo += controlUnicode
            else:
                strConteudo += paragrafos
        for paragrafos in contentP:
            if matchNews(paragrafos):
                self.match_counter += 1
            controlUnicode = ''
            if u'\xa0' in paragrafos:
                controlUnicode = paragrafos.replace(u'\xa0', u' ')
            if controlUnicode:
                strConteudo += controlUnicode
            else:
                strConteudo += paragrafos
        if self.match_counter > 0 and strConteudo != "": 
            news = NewsItem()
            news['title'] = title
            news['conteudo'] = strConteudo
            news['url'] = response.request.url
            self.newsCounter += 1
            yield news
