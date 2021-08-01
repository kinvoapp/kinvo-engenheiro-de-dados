import scrapy
from scrapy.selector import Selector
from scrapy.http import XmlResponse
import requests
import json
import time
from flask import jsonify

import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

#browser settings
options = Options()
options.add_argument("--allow-running-insecure-content")
options.add_argument("no-sandbox");
options.add_argument("headless"); 
options.add_argument("start-maximized");
options.add_argument("window-size=1900,1080");
options.add_argument("no-sandbox")
options.add_argument("--no-sandbox");
options.add_argument("--ignore-certificate-errors");
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')

capabilities = {
'browserName': 'chrome',
'chromeOptions':  {
   'useAutomationExtension': False,
   'forceDevToolsScreenshot': True,
   'args': ['--start-maximized', '--disable-infobars']
 }
} 


#path do chromedriver no linux
#chromedriverPath = 'chromedriver_linux/chromedriver'

#caso windows:
chromedriverPath = 'chromedriver_win/chromedriver.exe'




def getNewsFinance(url):
    
    r = requests.get(url)
    selector = Selector(text=r.content, type='xml')
    
    
    noticias = selector.xpath('//channel/item')
    
    #lista que guardará o dicionario de noticias
    content = []
    id = 0
    
    for noticia in noticias:
        
        #Para com o limite de noticias
        if len(content) >= 5:
            break

        titulo = noticia.xpath('title/text()').extract_first()
        categorias = noticia.xpath('category/text()').extract()

        shouldproceed = False

        #Checa se a noticia tem categoria de 'MANCHETE', pois sempre são noticias sobre a Bolsa
        for categoria in categorias:
            if 'MANCHETE' in categoria:
                shouldproceed = True
         
        if shouldproceed == True:

            linkNoticia = noticia.xpath('link/text()').extract_first()
            
            #pega sourcecode da noticia
            r = requests.get(linkNoticia)
            selector = Selector(text=r.content, type='html')
            
            
            #Retirando texto mesmo quando as children nodes são diferentes
            
            texto = list()
            for r in selector.xpath('/html/body/div[2]/div[2]/div/div[1]/div[3]'):
                 text = [p.strip() for p in r.xpath('.//text()').extract() if p.strip()]
                 texto.append(' '.join(text))
           

            noticiaDict = {
                 'title': titulo,
                 'id': id,
                 'texto': texto[0]
            }

            print(texto[0])

            content.append(noticiaDict)
            #loop id
            id = id + 1
    

    #Finaliza convertendo para json a lista de noticias   
    with open('data/noticiasFinance.json', 'w') as json_file:
        json.dump(content, json_file, ensure_ascii=False)

    return content
   
    



def getNewsInstante(url):
    
    
    
    r = requests.get(url)
    selector = Selector(text=r.content, type='xml')
    

    noticias = selector.xpath('//channel/item')
    
    #Lista onde serão adicionadas as noticias
    content = []
    id = 0
    
    
    
    for noticia in noticias:
        titulo = noticia.xpath('title/text()').extract_first()
        link = noticia.xpath('link/text()').extract_first()
        categorias = noticia.xpath('category/text()').extract()

        if len(content) >= 5:
            break

        shouldproceed = False
        for categoria in categorias:
            #Continua se for uma noticia da categoria Bolsa de Valores
            if 'Bolsa de Valores' in categoria:
                shouldproceed = True    
       

        if shouldproceed == True:
           
            """O site do UltimoInstante precisa de Javascript para ser executado, para lidar com isso foi utilizado um headless 
                browser com o Selenium"""   
            driver = webdriver.Chrome(executable_path=chromedriverPath, options=options)
            driver.get(link)
            contentPath = '//html/body/div[3]/div[4]/div[1]/div[1]/div/div[3]/div/div[1]/div[1]/div/div[4]/div[2]/div[2]'
                
            #Espera o elemento ser carregado antes de retornar o código fonte para o Scrapy
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, contentPath)))
            except:
                continue
            selector = Selector(text=driver.page_source, type='html')
            driver.close()
               
                
            #Recolhe tags p
            text = list() 
            pTags = selector.xpath(contentPath)
            for p in pTags:
                texts = p.xpath('p/text()').extract()
                for t in texts:
                    text.append(t)
        
            texto = ''.join(text)
            print(texto)

            noticiaDict = {
                 'title': titulo,
                 'id': id,
                 'texto': texto
            }

            content.append(noticiaDict)

            id = id + 1




    #Finaliza convertendo para json a lista de noticias    
    with open('data/noticiasInstante.json', 'w') as json_file:
        json.dump(content, json_file, ensure_ascii=False)
    return content
  


#Informação sobre o RSS
def homeHeader(url):
    
    r = requests.get(url)
    selector = Selector(text=r.content, type='xml')
    
    
    title = selector.xpath('//channel/title/text()').extract_first()
    link = selector.xpath('//channel/link/text()').extract_first()
    descricao = selector.xpath('//channel/description/text()').extract_first()

    content = {
        'link': link,
        'description': descricao,
        'title': title
    }

    return content









    
    
