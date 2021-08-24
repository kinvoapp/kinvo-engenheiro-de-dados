> ![Logo Kinvo](https://github.com/kinvoapp/kinvo-mobile-test/blob/master/logo.svg)

# Teste para candidatos à vaga de Desenvolvedor Python (com foco em IA - inteligencia Artificial)  


Como executar o projeto:

1 - Primeiro, instale os módulos necessários (Para evitar conflitos entre módulos, é preferível que tais comandos sejam executando em um ambiente virtual, como venv ou conda)
  ```
  pip install flask
  pip install spacy
  pip install scrapy
  pip install scrapyrt
  ```
(Opcional) Caso queira modificar o treinamento do modelo NLP, será necessário fazer o download do modelo base com o seguinte comando
```
python -m spacy download pt_core_news_md
```
2 - Após a instalação, acesse o diretório onde está spider para executar o scrapyrt

```
cd crawler
scrapyrt
```
3 - Com o scrapyrt rodando, abra outro terminal e acesse o diretório da aplicação web, e inicie a mesma.

```
cd webapp
flask run
```

4 - Pronto! Agora navegue até a página http://127.0.0.1:5000/ , onde estão localizadas os menus de navegação, bem como os dois end-points da API.

Observações:

O site utilizado foi o https://financenews.com.br/. Para contornar a sua estrutura foram estabelicidos alguns parâmetros, por exemplo, para encontrar notícias sobre ações da B3, o scraper primeiro análisa dois casos, o primeiro e se o nome de umas das empresas listadas na B3 ou o código da ação listada na bolsa se encontra em algum paragráfo da notícia, caso encontrado, se inicia a busca por algumas palavras chaves que são comuns em notícias do ramo, afim de evitar falsos-positivos.
A obtenção dessa lista de nomes de empresas bem como os seus respectivos códigos de suas ações também podem ser coletados de forma automática, basta executar a spider "getCod".

Também foi necessário uma maneira para não se repetir notícias muito similares, visto que toda terca-feira e sexta-feira, o site lança uma coletânea sobre notícias corporativas, onde muitas vezes se repete o conteúdo, então somente a notícia mais recente dessa coletânea é coletada pelo scraper.

Na pasta "Content", se encontra o modelo de NLP utilizado na aplicação.

O modelo de NLP utilizado foi o pt_core_news_md, com a adição de três labels, uma para identificar o código das ações encontradas na notícia, uma para identificar preços e outra para identificar textos contendo porcentagem. As outras labels já existentes no modelo também foram treinadas em conjunto com as novas labels. As informações contendo os dados utilizados para treinar o modelo, bem como todo código envolvido podem ser encontradas no arquivo "trainingModel.py".
