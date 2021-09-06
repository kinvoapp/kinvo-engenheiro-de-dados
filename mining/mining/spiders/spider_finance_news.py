import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ScrapyFinanceNews(CrawlSpider):
    name = 'finance-news'
    start_urls = ['https://financenews.com.br/category/nao-deixe-de-ler/?s=B3']

    custom_settings = {
        'DEPTH_LIMIT': '2',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=("*//div[@class='archive-item']")
            ),
            callback='parse'
        ),
        Rule(
            LinkExtractor(
                restrict_css=(".nextpostslink")
            )
        )
    )

    def parse(self, response):
        tag = response.xpath("*//div[@class='post-tags']/a/text()").get()
        description = response.xpath(".//div[@class='title-single']/h1/text()").get()
        if 'B3' in re.sub(r'[^\w\s]','',description).strip().split():
            yield {'tag': tag, 'description': description.strip()}
    