> ![Logo Kinvo](https://github.com/kinvoapp/kinvo-mobile-test/blob/master/logo.svg)

# Teste para candidatos à vaga de Desenvolvedor Python (com foco em IA - inteligencia Artificial)  


Como executar o projeto:

1 - Primeiro, instale os módulos necessários
  ```
  pip install flask
  pip install spacy
  python -m spacy download pt_core_news_md (talvez esse passo só seja necessário se o usuário quiser retreinar o modelo, testar antes de enviar)
  pip install scrapy
  pip install scrapyrt
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

4 - Pronto! Agora navegue até as páginas /minerar para minerar as notícias, e /processar para processar as mesmas. Também foram adicionadas outras páginas para facilitar a visualização das informações.

Observações:

O modelo de NLP utilizado foi o pt_core_news_md, com a adição de três labels, uma para identificar o código das ações encontradas na notícia, uma para identificar preços e outra para identificar textos contendo porcentagem. As outras labels já existentes no modelo também foram treinadas em conjunto com as novas labels. As informações contendo os dados utilizados para treinar o modelo, bem como todo código envolvido podem ser encontradas no arquivo "trainingModel.py".
