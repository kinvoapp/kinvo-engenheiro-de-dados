- Crie um ambiente virtual em python 3
  `virtualenv -p python3 _vv`

- Ative o ambiente:
  `source _vv/bin/activate`

- Instale os requerimentos:
  `pip install -r requirements.txt`

- Instale o modelo para o Spacy:
  `python -m spacy download pt_core_news_sm`

- Rode o app:
  `python app.py`

O app vai rodar em localhost:8080.

Existem três endpoints disṕoníveis:

- /api/mine_save \
  Comando via terminal: `curl -X GET localhost:8080/api/mine_save`\
  Ao acessar esse endpoint o feed de notícias dos sites ultimoinstante e financenews é minerado tendo em vista ações da B3 e gera um arquivo que é salvo com o nome finance.jsonl na pasta files.

- /api/extract_entities/<int:num> \
  Comando via terminal: `curl -X GET localhost:8080/api/extract_entities/5` \
  Esse endpoint retorna as últimas <int:num> notícias mineradas com a análise das entidades reconhecidas no título pelo Spacy.

---

Observações:

- Para usar os endpoints é pressuposto que existe um arquivo chamado b3.csv na pasta files, contendo as informações da B3.
  Foi criado um endpoint que realiza a extração dessas informações: 
  - /get_b3 \
  `curl -X GET localhost:8080/get_b3`

- Ao minerar e salvar as notícias elas são incluídas no topo do arquivo finance.jsonl, sem apagar as anteriores.
- Ao extrair as notícias as mesmas são lidas a partir do topo do arquivo.

\*\*\* A mineração das notícias e a extração das entidades não está 100% precisa. Para melhorar os resultados seria necessário treinar o Spacy para reconhecer as entidades da B3 e carregar o modelo já treinado.

\*\* Foi criada uma pasta de testes. Alguns testes ainda não passam e dependem do treinamento do modelo Spacy. Para rodar os testes, deve-se executar fora da pasta testes:
`python -m unittest tests/test_spider.py`
