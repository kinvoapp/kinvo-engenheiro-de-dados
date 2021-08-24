import scrapy
from scrapy import selector


class getCod(scrapy.Spider):
    name = 'getCod'
    allowed_domains = ['guiainvest.com.br']
    start_urls = ['https://www.guiainvest.com.br/lista-acoes/default.aspx?listaacaopage=1']
    base_url = 'https://www.guiainvest.com.br'
    
    def parse(self, response):
        try:
            next_page = response.xpath("//a[@title='Próxima Página']/@href").extract_first()
            print(type(next_page))
            full_np_url = self.base_url + next_page
            yield scrapy.Request(full_np_url, callback=self.parse)
        except TypeError:
            pass
        for ac in response.xpath(".//tr[contains(@class ,'rgAltRow') or contains(@class, 'rgRow')]"):
            cod = ac.xpath(".//a[@id='hlNome']/text()").get()
            pregao = ac.css("td:nth-child(3)::text").get()
            yield {
                'Codigo' : cod,
                'Pregao' : pregao
            }
    