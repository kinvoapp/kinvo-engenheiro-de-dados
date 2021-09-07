import re
import html
import scrapy
import w3lib.html

from kinvo.logger import logger


class FinanceSpider(scrapy.Spider):
    name = 'financenews'
    allowed_domains = ['financenews.com.br']
    start_urls = ["https://financenews.com.br/feed/",
                  "https://ultimoinstante.com.br/feed/"]

    def parse(self, response):
        if 'financenews.com.br' in response.url:
            self.parse_finance(response)
        else:
            self.parse_instant(response)

    def parse_instant(self, response):
        stocks_kw = ['ibovespa', 'ações', 'B3']

        logger.info(f"Parsing {response.url}")

        for item in response.css('item'):
            categories = item.css('category::text').getall()

            has_keywords = any(kw in categories for kw in stocks_kw)

            if has_keywords:
                title = item.css('title::text').get()
                pub_date = item.css('pubDate::text').get()
                link = item.css('link::text').get()

                content = item.css('description::text').get()
                content = w3lib.html(content).replace('\n', ' ')
                content = html.unescape(content.strip())

                yield {'title': title, 'link': link,
                       "pub_date": pub_date, 'content': content}

    def parse_finance(self, response):
        stock_regex = r"[A-Za-z]{4}\d{1,2}"
        stocks_kw = ['ibovespa', 'ações', 'B3']
        reject_kw = ['notícias corporativas']

        logger.info(f"Parsing {response.url}")

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
                yield scrapy.Request(url=url, callback=self.load_finance)

    def load_finance(self, response):
        title = response.css('title::text').get().strip()
        link = response.url
        pub_date = response.css('.pull-left::text').get().strip()

        content = ' '.join([t.strip()
                            for t in response.css('.page-post>p>span::text').getall()])

        if content:
            logger.info("Loaded News:")
            logger.info((f"Title: {title}, "
                         f"link: {link}, "
                         f"Published on: {pub_date}"))

            yield {'title': title, 'link': link,
                   "pub_date": pub_date, 'content': content}
