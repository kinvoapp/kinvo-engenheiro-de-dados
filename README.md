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

Na pasta "Content", se encontra o modelo de NLP utilizado na aplicação.
O modelo de NLP utilizado foi o pt_core_news_md, com a adição de três labels, uma para identificar o código das ações encontradas na notícia, uma para identificar preços e outra para identificar textos contendo porcentagem. As outras labels já existentes no modelo também foram treinadas em conjunto com as novas labels. As informações contendo os dados utilizados para treinar o modelo, bem como todo código envolvido podem ser encontradas no arquivo "trainingModel.py".
