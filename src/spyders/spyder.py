import scrapy
import json


conteudo = {}


class Spyder(scrapy.Spider):
    name = 'main-spyder'
    start_urls = ['https://financenews.com.br/2021/02/copel-sofre-ataque-cibernetico/']
    allowed_domains = ['financenews.com.br']


    def parse(self, response):
        titulo = response.xpath('//h1/text()').get()

        texto = ""
        for paragrafo in response.xpath('//div/p/span/text()').getall():
            texto += paragrafo.replace(u'\xa0', " ")

        if titulo and len(texto) > 300:
            conteudo[titulo.strip()] = texto
        del texto, titulo

        for next_page in response.css('a'):
            if len(conteudo) < 2:
                yield response.follow(next_page, self.parse)
            else:
                with open('../data/titulo_conteudo.json', 'w', encoding='utf8') as outfile:
                    json.dump(conteudo, outfile, ensure_ascii=False)

