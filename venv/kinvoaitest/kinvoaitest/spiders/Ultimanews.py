import scrapy
from kinvoaitest.items import NewsItem
from scrapy.loader import ItemLoader
class UNewsSpider(scrapy.Spider):
    name= 'unews'

    start_urls=[
        'https://www.ultimoinstante.com.br/tag/b3/'
    ]
    def parse(self, response):
        Noticia=response.xpath("//h3[@class='jeg_post_title']/a/text()").get()
        yield {

                    'Noticia':Noticia        
            }