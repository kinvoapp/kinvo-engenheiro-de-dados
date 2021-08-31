from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from scrapy.exporters import CsvItemExporter
FEED_EXPORT_ENCODING = 'utf-8',
#from kinvoaitest.items import NewsItem
#from scrapy.loader import ItemLoader
class NewsSpider(scrapy.Spider):
    name= 'finews'
    start_urls=[
        'https://financenews.com.br/2021/08/companhias-da-b3-que-divulgaram-informacoes-sobre-proventos-na-semana-3/',
    ]
# Para realizar o pln vou agregar toda a extração
    def parse(self, response):
        for fnews in response.xpath("//div[@class='page-post']"):
            yield {
            'Acao': fnews.xpath("//div[@class='page-post']/descendant::h1/text()").getall(),
            'Notícia': fnews.xpath("//p/text()").getall()
            }
           
        
c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
    'FEED_FORMAT': 'CSV', 
    'FEED_URI':'file://tmp/export.csv',
        })
c.crawl(NewsSpider)
c.start()

