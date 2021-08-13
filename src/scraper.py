import scrapy

 
class B3Crawler_finance(scrapy.Spider):
    name = "B3"
    start_urls = ['https://financenews.com.br/?s=b3']
 
    def parse(self, response):
        for b3 in response.css('div.col-md-8'):
            yield {
                'feed': b3.css('a::text').get(),
            }