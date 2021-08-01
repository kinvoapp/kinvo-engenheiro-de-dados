# API Notícias
## Essa API retorna noticias sobre a B3 e entidades

### Documentação
#### Sites disponíveis

1. Finance News: "finance"
2. Ultimo Instante: "instante"

#### End Points

1. "/": Info sobre API
2. "/website": Info sobre o RSS
3. "/website/news": Lista de noticias sobre a B3
4. "/website/news/entities": Entidades das noticias

#### Exemplo

##### /finance/news
{ "fonte": "https://financenews.com.br", "id": 1, "title": "São Martinho vai pagar dividendos" }...

##### /finance/news/entities
{"id": 1,
"title": "São Martinho vai pagar dividendos",
"entidades": [ "entidade": "B3", "tipo": "ORG" },
{ "entidade": "Porto Seguro", "tipo": "LOC" }
] }...


## Considerações

1. Foram consideradas apenas as noticias encontradas no RSS dos sites(/feed)
2. No site da Último Instante, a categoria "Bolsa de Valores" foi utilizada como parâmetro, porém nem sempre se tem noticias desta categoria no RSS
3. Como o site da Último Instante precisa de Javascript para ser carregado, foi utilizado um headless browser(chromedriver) para retornar o código fonte da página
4. A trained pipeline utilizada no Spacy foi a: pt-core-news-sm 

## Instruções

1. Basta executar o api.py 
2. crawler.py têm as funções de mineração e entityGetter.py as do Spacy.
3. A depender do OS a localização do chromedriver(utilizado no selenium) deve ser alterada: 
    * crawler.py, line41: "chromedriverPath = 'chromedriver_linux/chromedriver' ou 'chromedriver_win/chromedriver.exe'
4. A versão do Chromedriver disponibilizada na pasta são a 92 e 91, para o Windows e Linux respectivamente, é necessário que a versão do chromedriver seja a mesma que a do Chrome instalado no OS.
