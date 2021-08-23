import scrapy


class FeedSpider(scrapy.Spider):
    name = 'feedspider'
    start_urls = ['https://financenews.com.br/feed/',
                  "https://www.ultimoinstante.com.br/feed/"]

    def parse(self, response):
        for item in response.css('item'):
            info = {
                'title': item.css('title::text').get(),
                'link': item.css('link::text').get(),
            }
            next_page = item.css('link::text').get()
            if next_page is not None:
                if "https://www.ultimoinstante.com.br/" in next_page:
                    yield response.follow(next_page, callback=self.parse_ultimoinstante,cb_kwargs=dict(info=info))
                elif "https://financenews.com.br/" in next_page:
                    yield response.follow(next_page, callback=self.parse_financenews,cb_kwargs=dict(info=info))

    def parse_ultimoinstante(self, response, info):
        # Redirect may need selenium
        print(response.css('title::text').get())

    def parse_financenews(self, response, info):
        post_content = " ".join(response.css(
            'div.page-post').css('span::text').getall())
        yield {**info, "content": post_content}