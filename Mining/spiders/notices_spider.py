import scrapy


class NoticeSpider(scrapy.Spider):
    name = "notices"
    start_urls = [
        'http://www.b3.com.br/pt_br/noticias/',
    ]

    def parse(self, response):
        for notice in response.css('div.card'):
            yield {
                'Data': notice.css('p::text')[0].get(),
                'Titulo': notice.css('h4::text').get(),
                'Noticia': notice.css('p::text')[1].get(),
            }
