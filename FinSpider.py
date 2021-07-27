import scrapy


class FinspiderSpider(scrapy.Spider):
    name = 'FinSpider'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/tudo-sobre/bmf-bovespa/']

    def parse(self, response):
        news_list = response.css('.bastian-page .bastian-feed-item')

        for news in news_list:
            titulo = news.css('.feed-post-link::text').extract_first()
            descricao = news.css('.feed-post-body-resumo::text').extract_first()
            link = news.css('.feed-post-link::attr(href)').extract_first()

            yield({'Titulo': titulo, 'Descricao': descricao, 'Link': link})
