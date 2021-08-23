import scrapy 
class Myspider(scrapy.Spider):
    name = 'news'
    allowed_domains = ["financenews.com.br"]
    start_urls = ['https://financenews.com.br/feed/']

    def parse(self,response):
        links = response.xpath('//channel/item')

        #extraindo os links do site.
        for link in links[:6]:
    
            linkExtracted = link.xpath('link/text()').get()
            yield scrapy.Request(url=linkExtracted, callback=self.extract_news)


    def extract_news(self,response):
        
        title = response.xpath('normalize-space(//div[@class="title-single"]//h1)').get()

        #Lista para as noticias extraidas
        texto = list()

        #extraindo as noticias dos links e removendo partes desnecessarias
        for r in response.xpath('/html/body/div[2]/div[2]/div/div[1]/div[3]'):
            text = [t.strip() for t in r.xpath('.//text()').extract() if t.strip()]
            texto.append(' '.join(text))


        yield{
            'title':title,
            'news':text
        }