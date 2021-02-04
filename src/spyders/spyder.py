import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Spyder(CrawlSpider):
    name = 'finance-news'
    start_urls = ['https://financenews.com.br']
    allowed_domains = ['financenews.com.br']

    custom_settings = {
        'DEPTH_LIMIT': '7',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=(
                "//nav//a[contains(text(),'Não deixe de ler')]")
            )
        ),
        Rule(
            LinkExtractor(
                restrict_css=(".nextpostslink")
            )
        ),
        Rule(
            LinkExtractor(
                restrict_css=(".archive-item")
            ),
            callback='parse_noticia'
        ),
        Rule(
            LinkExtractor(
                restrict_css=(".mais-lidas")
            ),
            callback='parse_noticia'
        )

    )

    def parse_noticia(self, response):
        article = " ".join(response.css('.page-post').xpath("//p[not(contains(.//text(), 'aqui')" +
                                                  " or contains(.//text(), 'Leia mais sobre')" +
                                                  " or contains(.//text(), 'o tema de compras coletivas de ações')" +
                                                  " or contains(.//text(), 'Para receber notícias')" +
                                                  " or contains(.//text(), 'hatsapp')" +
                                                  " or contains(.//text(), 'entre nesse grupo')" +
                                                  " or contains(.//text(), 'Publicado às')" +
                                                  " or contains(.//text(), 'Atualizado às')" +
                                                  " or contains(.//text(), 'elegram')" +
                                                  " or contains(.//text(), 'Finance News')" +
                                                  " or contains(.//text(), 'clique')" +
                                                  " or contains(.//text(), 'leia)" +
                                                  " or contains(.//text(), 't.me/'))]//text()").getall()).replace(
            '\xa0', '')

        if len(article) > 199:
            yield {response.url: article.strip()}
