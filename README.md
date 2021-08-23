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
# Amostra da aplicação desenvolvida
### Considerações
```
Para minha implementação foi utlizada apenas o site https://financenews.com.br,
Tambem renderizei os resultados obtidos pelas apis para uma melhor visualização.
 ```

**Renderização das noticias mineradas e salvas** 
![Captura de tela de 2021-08-22 23-31-57](https://user-images.githubusercontent.com/67839316/130382069-4152671e-1d1f-43bc-9ab8-1a39b9aea9b2.png)

**Renderização das entidades extraidas das noticias mineradas**
![Captura de tela de 2021-08-22 23-08-42](https://user-images.githubusercontent.com/67839316/130381900-8886197c-ca93-4ab9-82f4-acc74682cdf0.png)


 ```
## Como rodar o projeto
```
* Instalações necessárias:	

		pip install flask
	
		pip install panda
	
		pip install spacy
	
		pip install scrapy
	
		python -m spacy download pt_core_news_sm


* execute o comando abaixo no terminal,dentro do diretorio, para rodar a aplicação:

	 	flask run

* No http://localhost:5000 use os seguintes endpoints:

   º Para minerar e salvar as noticias, endpoint /getnews (Deve entrar aqui primeiro para gerar o arquivo das noticias)

		http://localhost:5000/getnews

   º Para extrair as entidade das noticias, endpoint /getentity.
   
		http://localhost:5000/getentity

```
