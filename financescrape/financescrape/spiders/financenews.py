import scrapy
from ..items import FinancescrapeItem

class FinanceNews(scrapy.Spider):
    name= "financenews"

    custom_settings = {
        'ITEM_PIPELINES': {
            'financescrape.pipelines.FinancescrapePipeline': 300,
        }
    }

    start_urls = ['https://financenews.com.br/feed/']

    def parse(self, response):
        response.selector.remove_namespaces()
        for item in response.css('item'):
            title = item.css('title::text').get()
            description = item.css('encoded')
            for scope in description:
                content = scope.xpath('text()').get()
                yield FinancescrapeItem(origin=self.name, title=title, content=content)