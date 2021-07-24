import scrapy

# Classe para fazer o download do feed do financenews e salvar em um arquivo html
class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    links = []

    def start_requests(self):
        url = "https://financenews.com.br/feed/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = f'news-financenews.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')