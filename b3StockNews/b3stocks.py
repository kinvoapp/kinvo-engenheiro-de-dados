import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor, defer

# scrapy class


class b3FinanceNews(scrapy.Spider):
    name = 'financenews'
    allowed_domains = ['financenews.com.br', 'ultimoinstante.com.br']
    start_urls = ['https://financenews.com.br/feed/',
                  'https://www.ultimoinstante.com.br/feed/']

    # o metodo parse padrão
    def parse(self, response):
        links = response.xpath('//channel/item/link/text()').getall()

        # fazendo loop pelos links
        for link in links:
            if "B3" in str(link).upper():
                print(link)
                request = response.urljoin(link)
                yield scrapy.Request(
                    request, self.parse_links)

    # metodo para escrever o conteudo das noticias
    def parse_links(self, response):
        content = response.xpath(
            '//html/body/div[2]/div[2]/div/div[1]/div[3]/p/text()').getall()
        content.append(response.xpath(
            '//html/body/div[3]/div[4]/div[1]/div[1]/div/div[3]/div/div[1]/div[1]/div/div[4]/div[2]/div[2]/p/text()').getall())

        with open('content.txt', 'r+', encoding="utf-8") as f:
            for c in content:
                print('--------- Writing to disk ------------')
                print(c)
                f.write(c)

        return None


runner = CrawlerProcess()

# caso queria adicionar crawlers


@defer.inlineCallbacks
def crawl():
    yield runner.crawl(b3FinanceNews)
    reactor.stop()


crawl()
reactor.run()
