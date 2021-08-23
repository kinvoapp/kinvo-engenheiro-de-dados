import scrapy
 
class FinanceNewsSpider(scrapy.Spider):
    name = 'finance-news'
    allowed_domains = ['financenews.com.br']
    start_urls = ['https://financenews.com.br/feed/']
    limit = 5
 
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for item in response.xpath('//channel/item')[:self.limit]:
            yield {
                'title' : item.xpath('title//text()').extract_first(),
                'pubDate' : item.xpath('pubDate//text()').extract_first(),
                'link': item.xpath('link//text()').extract_first()
            }