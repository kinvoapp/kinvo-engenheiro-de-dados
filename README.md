> ![Logo Kinvo](https://github.com/kinvoapp/kinvo-mobile-test/blob/master/logo.svg)

# Teste para candidatos à vaga de Desenvolvedor Python (com foco em IA - inteligencia Artificial)  

## Instruções:

1. Minerar 5 notícias sobre ações da B3. importante salvar para ser usada no processamento de linguagem natural(PNL) posteriormente. 

2. Extrair as entidades das 5 notícias mineradas anteriormente(entity recognition).

3. Extrair entidades customizada das notícias(entity recognition).


```
Exemplo 1 de extração customizada:

"Randon (RAPT3 e RAPT4) registrou lucro de R$ 49.99 milhões no 4º trimestre de 2018"

Após executar o entity recognition(customizado) seguem abaixo os dados extraídos:
Events: registrou, lucro
Org: Random
Product: RAPT3, RAPT4

Exemplo 2 de extração customizada:

"Ibovespa registra queda pressionado pela petrobrás"

Após executar o entity recognition(customizado) seguem abaixo os dados extraídos:
Events: registra, queda
Org: Ibovespa, petrobrás
Product: ""


Criar uma api com dois end-points para:
	- minerar e salvar as noticías;
	- extrair as entidades das notícias mineradas(entity recognition);


  ```

4. Após terminar seu teste submeta um pull request e aguarde seu feedback.


### Pré-requisitos:

* Utilizar Flask;
* Utilizar Python;
* Utilizar Spacy;
* Utilizar Scrapy;


* **Importante:** Usamos o mesmo teste para todos os níveis de front: **junior**, **pleno** ou **senior**, mas procuramos adequar nossa exigência na avaliação com cada um desses níveis sem, por exemplo, exigir excelência de quem está começando :-)

## Submissão

Para iniciar o teste, faça um fork deste repositório, crie uma branch com o seu nome e depois envie-nos o pull request.
Se você apenas clonar o repositório não vai conseguir fazer push e depois vai ser mais complicado fazer o pull request.

**Sucesso!**
