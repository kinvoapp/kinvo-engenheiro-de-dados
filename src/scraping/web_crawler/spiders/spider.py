from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import json
with open('data/empresas_B3.json','r') as b3_file:
    b3=json.load(b3_file)
with open('data/words.json','r') as words_file:
    words=json.load(words_file)


def contain(string, arr, value):
    count = 0
    for i in range(len(arr)):
        if arr[i] in string:
            count +=1
            if count == value:
                return True
    return False


class Spyder(CrawlSpider):
    name = 'finance-news'
    start_urls = ['https://financenews.com.br']
    allowed_domains = ['financenews.com.br']

    custom_settings = {
        'DEPTH_LIMIT': '8',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=(
                "//nav//a[contains(text(),'Não deixe de ler')]")
            )
        ),
        Rule(
            LinkExtractor(
                restrict_css=(".nextpostslink")
            )
        ),
        Rule(
            LinkExtractor(
                restrict_css=(".archive-item")
            ),
            callback='parse_noticia'
        ),
        Rule(
            LinkExtractor(
                restrict_css=(".mais-lidas")
            ),
            callback='parse_noticia'
        )

    )

    def parse_noticia(self, response):
        paragrafos = []

        data = response.css('.pull-left').xpath('.//text()').get().strip()

        for paragrafo in response.css('.page-post').xpath("//p/span/text()").getall():
            paragrafo = paragrafo.replace('\xa0', '')
            paragrafo = paragrafo.strip()

            if len(paragrafo) > 50 and contain(paragrafo, b3, 1) and contain(paragrafo, b3, 2):
                yield {'news': data + " " + paragrafo}

        for paragrafo in response.css('.page-post').xpath("//p/text()").getall():
            paragrafo = paragrafo.replace('\xa0', '')
            paragrafo = paragrafo.strip()

            if len(paragrafo) > 50 and contain(paragrafo, b3, 1) and contain(paragrafo.lower(), words, 2):
                yield {'news': data + " " + paragrafo}