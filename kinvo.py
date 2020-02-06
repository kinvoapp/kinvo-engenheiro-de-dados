from requests import get
from bs4 import BeautifulSoup
import re

#LISTA COM NOMES DA EMPRESA
lista_empresa = ['oi','jbs','helbor','cemig','cielo']
produtos = {'oi':'OIBR3/OIBR4', 'jbs':'JBSS3','helbor':'HBOR3','cemig':'CMIG3/CMIG4','m.dias':'MDIA3','cielo':'CIEL3'}


#CODIGO PARA 1º RASPAGEM:
url = 'http://br.advfn.com/jornal/acoes/balanco-trimestral'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
noticias_gerais = html_soup.find_all('div', class_ = 'posts-list listing-alt')
container01_noticia = html_soup.find_all('div', class_ = 'content')
count = 0

#IDENTIFICAR NOTICIA E LINK DA NOTICIA:
def inicio():
    print('NOTICIA:',noticia.a.text) 
    print('LINK:', link_noticia)

#IDENTIFICAR O RESULTADO (LUCRO/PREJUIZO) DE ACORDO COM O TEMA DA NOTICIA:
def resultado():
    if re.search('prejuízo',noticia.a.text, re.IGNORECASE):
        print('RESULTADO: houve prejuízo (⤵️)')
    elif re.search('queda',noticia.a.text, re.IGNORECASE):
        print('RESULTADO: houve prejuízo (⤵️)')
    elif re.search('lucro',noticia.a.text, re.IGNORECASE):
        print('RESULTADO: houve lucro (⤴️)')
    elif re.search('cresce',noticia.a.text, re.IGNORECASE):
        print('RESULTADO: houve lucro (⤴️)')
    else:
        print('RESULTADO: não identificado') 

#IDENTIFICAR NOME DA EMPRESA & PRODUTO
def nome_empresa():
    count_tags = -1
    count_empresa = 0
    product = []
    #NOME EMPRESA
    while (count_tags  < len(first_movie)-1):
        count_tags = count_tags + 1
        tags = first_movie[count_tags].text.lower()
        if tags in lista_empresa:
            print('NOME DA EMPRESA:',tags)
            count_empresa = count_empresa + 1
            product = tags
            break

    if count_empresa == 0:
        print('NOME DA EMPRESA: não identificada')
        product = 'none'
    #NOME DO PRODUTO DA EMPRESA
    if product == 'none':
        print('PRODUTO: não identificado')
    else:
        print('PRODUTO: ',produtos[product])

# MINERAÇÃO DAS NOTICIAS
while (count < 6): # INFORME A QUANTIDADE DE NOTICIAS
    noticia = container01_noticia[count]
    link_noticia = noticia.a.get('href') #Aqui irá pegar o URL do artigo
    url2 = link_noticia
    response2 = get(url2)
    html_soup2 = BeautifulSoup(response2.text, 'html.parser')
    type(html_soup2)
    container02_noticia = html_soup2.find('div', class_ = 'tagcloud')

    first_movie = container02_noticia.find_all('a')
    print()
    print('------------------',count+1,'º Noticia ------------------')
    inicio()
    nome_empresa()
    resultado()
    count = count + 1