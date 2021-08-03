import scrapy 
import re

class raspagem_noticias(scrapy.Spider):

    name = "noticias"

    start_urls = ["https://www.ultimoinstante.com.br/feed/",
    "https://financenews.com.br/feed/"]

    def parse(self, response):

        titulos = response.xpath("channel/item/title/text()").getall()
        links = response.xpath("channel/item/link/text()").getall()
        descricaos = response.xpath("channel/item/description/text()").getall()

        for titulo, link, descri in zip(titulos, links, descricaos):

            empresa_b3 = re.findall("[a-zA-Z]{4}[0-9]", descri)

            if empresa_b3:
                
                yield scrapy.Request(link, callback=self.noticia, 
                meta={"titulo":titulo,
                "link":link,
                "descricao": descri.split("p>")[1][:-2]})

    def noticia(self, response):
        """ entrando no site da noticia, se estiver tudo dentro dos paramentros, a noticia e salvada"""

        titulo = response.meta['titulo']
        link = response.meta['link']
        descri = response.meta['descricao']

        noticia = response.xpath("string(/html/body/div[2]/div[2]/div/div[1]/div[3])").get().strip()

        trans_table = {ord(c): " " for c in u'\r\n\t\xa0'}
        noticia = ''.join(s.translate(trans_table) for s in noticia)
        noticia = noticia.split("Whatsapp")[0].strip()

        if len(noticia) > 200:
            
            yield{
            "titulo":titulo,
            "link":link,
            "descricao": descri,
            "noticia":noticia
            }