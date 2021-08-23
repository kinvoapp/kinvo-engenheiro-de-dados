import scrapy


class B3Spider(scrapy.Spider):
    name = "b3"
    start_urls = [
      "https://financenews.com.br/feed/",
      "https://www.ultimoinstante.com.br/feed/"
    ]

    def parse(self, response):
        for link in response.css('link::text'):
            yield {
              'link': link,
            }