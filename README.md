> ![Logo Kinvo](https://github.com/kinvoapp/kinvo-mobile-test/blob/master/logo.svg)

# Kinvo IA test

Pojeto teste para processo seletivo da Kinvo em back-end, com foco em inteligência artificial.
Para realizá-lo, foi orientado que é necessário minerar 5 notícias de sites recomendados pelos mesmos, sobre ações da B3. Foi salientada a importância de salvar para serem usadas no processamento de linguagem natural(PNL) posteriormente;
Extrair as entidades das notícias mineradas anteriormente e, por fim, criar uma API com dois end-points, sendo eles:
    
    -minerar e salvar notícias;
    -extrair as entidades das notícias mineradas.

Além de ser um projeto em python, as ferramentas solicitadas foram Flask, Spacy e Scrapy. 

## Como clonar o repositório

Faça o clone deste repositório

```sh
git clone  https://github.com/Beatrizdacruz/kinvo-ia-test.git
```

Entre na pasta clonada

```sh
cd kinvo-ia-test
```

Mude a branch

```sh
git checkout beatriz-cruz
```


## Como rodar o projeto

Antes de rodar o projeto em sua máquina, é importante lembrar que é preciso importar as bibliotecas utilizadas nos códigos no terminal do editor de código.
    
    1- No arquivo notice.py há o código necessário para minerar as notícias do site recomendado, ao qual foi gerado um novo arquivo (news.csv) para guardar as informações;
    
    2- No arquivo PLN.py há o código necessário para extrair as entidades das notícias mineradas;
    
    3- Por fim, o arquivo main.py, dentro da pasta new-api> templates, há a API, que, combinada ao arquivo html index.html, gera um microframework.