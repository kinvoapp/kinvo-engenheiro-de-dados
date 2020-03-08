import scrapy
from ..items import FinancescrapeItem

class UltimoInstante(scrapy.Spider):
    name= "ultimoinstante"

    custom_settings = {
        'ITEM_PIPELINES': {
            'financescrape.pipelines.FinancescrapePipeline': 300,
        }
    }

    start_urls = ['https://www.ultimoinstante.com.br/feed/']

    def parse(self, response):
        for item in response.css('item'):
            title = item.css('title::text').get()
            description = item.css('description')
            for scope in description:
                content = scope.xpath('text()').get()
                yield FinancescrapeItem(origin=self.name, title=title, content=content)