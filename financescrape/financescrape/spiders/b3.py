import scrapy
import string

class B3(scrapy.Spider):
    name = "b3"

    custom_settings = {
        'DOWNLOAD_DELAY' : 0.5
    }

    def start_requests(self):
        seq= list(string.ascii_uppercase)
        urls = [f"https://br.advfn.com/bolsa-de-valores/bovespa/{item}" for item in seq]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for active in response.xpath('//tr[contains(@class,"even" ) or contains(@class,"odd" ) ]'):
            name = active.css('td a::text').extract_first()
            symbol = active.css('td::text').extract_first()
            yield {
                'name': name,
                'symbol': symbol
            }