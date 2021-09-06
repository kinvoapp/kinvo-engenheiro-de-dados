import re
import scrapy

from kinvo.logger import logger


class FinanceSpider(scrapy.Spider):
    name = 'financenews'
    allowed_domains = ['financenews.com.br']
    start_urls = ["https://financenews.com.br/feed/"]

    def parse(self, response):
        stock_regex = r"[A-Za-z]{4}\d{1,2}"
        stocks_kw = ['ibovespa', 'ações', 'B3']
        reject_kw = ['notícias corporativas']

        logger.info("Parsing page")

        for item in response.css('item'):
            url = item.css('link::text').get()
            categories = item.css('category::text').getall()

            has_keywords = any(kw in categories for kw in stocks_kw) or \
                any(re.match(stock_regex, c) for c in categories)

            has_rejects = any(kw in categories for kw in reject_kw)

            logger.info((f"Item: {url}, "
                         f"has_keywords: {has_keywords}, "
                         f"has_rejects: {has_rejects}"))

            if not has_rejects and has_keywords:
                yield scrapy.Request(url=url, callback=self.load_news)

    def load_news(self, response):
        title = response.css('title::text').get().strip()
        link = response.url
        pub_date = response.css('.pull-left::text').get().strip()

        content = ' '.join([t.strip()
                            for t in response.css('.page-post>p>span::text').getall()])

        if content:
            logger.info("Loaded News:")
            logger.info((f"Title: {title}, "
                        f"link: {link}, "
                         f"Publish on: {pub_date}"))

            yield {'title': title, 'link': link,
                   "pub_date": pub_date, 'content': content}
