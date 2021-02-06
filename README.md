> ![Logo Kinvo](https://github.com/kinvoapp/kinvo-mobile-test/blob/master/logo.svg)

# Teste para candidatos à vaga de Desenvolvedor Python (com foco em IA - inteligencia Artificial)  


## Instruções:

1. Minerar 5 notícias sobre ações da B3. Importante salvar para ser usadas no processamento de linguagem natural(PNL) posteriormente. 
	 - https://financenews.com.br/feed/
	 - https://www.ultimoinstante.com.br/feed/

2. Extrair as entidades das 5 notícias mineradas anteriormente(entity recognition).


Criar uma api com dois end-points para:

	- minerar e salvar as noticías;
	- extrair as entidades das notícias mineradas(entity recognition);


  ```

3. Após terminar seu teste submeta um pull request e aguarde seu feedback.


### Pré-requisitos:

* Utilizar Flask;
* Utilizar Python;
* Utilizar Spacy;
* Utilizar Scrapy;


* **Importante:** Usamos o mesmo teste para todos os níveis de desenvolvedor, **junior**, **pleno** ou **senior**, mas procuramos adequar nossa exigência na avaliação com cada um desses níveis sem, por exemplo, exigir excelência de quem está começando :-)

## Submissão

Para iniciar o teste, faça um fork deste repositório, crie uma branch com o seu nome e depois envie-nos o pull request.
Se você apenas clonar o repositório não vai conseguir fazer push e depois vai ser mais complicado fazer o pull request.

**Sucesso!**

 ```
## Como instalar e rodar
```
* Primeiramente, garanta que você tem o python na versão 3.7 instalado

* Apartir daí, utilize os seguintes comandos para instalar as importações necessárias e o ambiente:
	pip install virtualenv
	python3.7 -m venv venv
	
	no windows: cd venv/Scripts/activate
	no linux: source venv/bin/activate
	
	pip install flask
	
	pip install setuptools wheel
	pip install spacy
	python -m spacy download pt_core_news_sm
	
	pip install scrapy
	pip install scrapyrt

* Navegue para a pasta /kinvo-ia-test/src/scraping

* Execute o comando abaixo e deixe esse terminal rodando:
	scrapyrt 

* Crie outro terminal com o virtualenv, navegue para a pasta /kinvo-ia-test/src e execute:
	no windows: set FLASK_APP=server.py
	no linux: export FLASK_APP=server.py
	flask run

* Abra seu navegador no http://localhost:5000

* Para minerar utiliza o endpoint /minerar, este passo deve ser realizado primeiro
	http://localhost:5000/minerar

* Logo em seguida para extrair as entidades utilize o endpoint /extrair.
	http://localhost:5000/extrair

```

## Aspectos e decisões de implementação

```

O site escolhido foi o https://financenews.com.br

Ele não possui padrão claro e definido sobre a escrita e elaboração de seu conteúdo.
Daí veio a ídeia de definir a nóticia sobre ações da bolsa, como um paragráfo que 
contém o nome de alguma ação da bolsa e algumas outras palavras de uso comum, quando
falado sobre. Por exemplo: 'alta' 'baixa' 'dividendos'. Está foi a maneira encotnrada
para driblar a estrutura do site.