import scrapy


class RssSpider(scrapy.Spider):
    name = 'rss'
    allowed_domains = ['Scrapy shellScrapy shell']
    start_urls = ['https://www.ultimoinstante.com.br/feed/']

    def parse(self, response):
        for noticia in response.xpath('//rss/channel/item')[0:5]:
            yield{
                'titulo': noticia.xpath('.//title/text()').get(),
                'descricao': noticia.xpath('.//description/text()').get()

            }
            

        #print(noticias)
        #pass
