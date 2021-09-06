import scrapy
from scrapy_splash import SplashRequest

RENDER_HTML_URL = "http://localhost:8050/render.html"

class ScrapyUltimoInstante(scrapy.Spider):
    name = 'ultimo-instante'
    start_urls = ["https://www.ultimoinstante.com.br/tag/b3/"]

    def parse(self, response):
        articles = response.xpath("*//article[@class='jeg_post jeg_pl_md_5 format-standard']")
        for article in articles:
            tag = article.xpath(".//span/a/text()").get()
            description = article.xpath(".//h3[@class='jeg_post_title']/a/text()").get()
            yield {'tag': tag, 'description': description}
        
        # next_page = response.xpath("*//a[@class='page_nav next']/@href").get()
        # if next_page is not None:
        #     yield SplashRequest(url=RENDER_HTML_URL+'?url='+next_page+'&timeout=50&wait=2', callback=self.parse)

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=RENDER_HTML_URL+'?url='+url+'&timeout=50&wait=2', callback=self.parse)
