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

# Solução Implementada

A solução implementada fornece dois endpoints onde os dados são formatados como JSON, para que um possível front-end pudesse ser facilmente acoplado, ou para que pudesse ser consumido por qualquer outra aplicação no estilo serviço de máquina para máquina. a API Flask guarda os dados que recebe do Scrapy temporariamente na memória pois um banco de dados seria desnecessário devido a simplicidade da aplicação.

## Rotas

### /get_scrapy (método GET)

Exemplo de saída:
```
[ {"title": "Renova Energia aumenta capital social reduz dívida concursal", "pubDate": "Tue, 24 Aug 2021 01:03:09 +0000", "link": "https://financenews.com.br/2021/08/renova-energia-aumenta-capital-social-reduz-divida-concursal/"}, {"title": "Notícias corporativas da noite desta segunda, 23", "pubDate": "Tue, 24 Aug 2021 00:17:54 +0000", "link": "https://financenews.com.br/2021/08/noticias-corporativas-da-noite-desta-segunda-23/"}, {"title": "Simpar vai recomprar até 11,4 milhões de ações", "pubDate": "Tue, 24 Aug 2021 00:06:41 +0000", "link": "https://financenews.com.br/2021/08/simpar-vai-recomprar-ate-114-milhoes-de-acoes/"}, {"title": "Petrobras inicia operação do FPSO Carioca no campo de Sépia", "pubDate": "Mon, 23 Aug 2021 23:48:55 +0000", "link": "https://financenews.com.br/2021/08/petrobras-inicia-operacao-do-fpso-carioca-no-campo-de-sepia/"}, {"title": "Banestes lança plano de desligamento voluntário", "pubDate": "Mon, 23 Aug 2021 23:44:19 +0000", "link": "https://financenews.com.br/2021/08/banestes-lanca-plano-de-desligamento-voluntario/"} ]
```
O formato é um JSON contendo uma lista de objetos com os atributos "title", "pubDate" e "link".

### /get_spacy (método GET)

Exemplo de saída:
```
[{"text": "Renova Energia aumenta capital social reduz dívida concursal", "entity_list": [{"entity": "Renova Energia", "type": "LOC"}]}, {"text": "Notícias corporativas da noite desta segunda, 23", "entity_list": []}, {"text": "Simpar vai recomprar até 11,4 milhões de ações", "entity_list": [{"entity": "Simpar", "type": "PER"}]}, {"text": "Petrobras inicia operação do FPSO Carioca no campo de Sépia", "entity_list": [{"entity": "Petrobras", "type": "ORG"}, {"entity": "FPSO Carioca", "type": "MISC"}, {"entity": "Sépia", "type": "PER"}]}, {"text": "Banestes lança plano de desligamento voluntário", "entity_list": [{"entity": "Banestes", "type": "PER"}]}]
```
O formato é um JSON contendo uma lista de objetos em que cada um deles possui atributos "text", que é o texto utilizado no reconhecimento de entidades e "entity_list", que traz uma lista de objetos contendo "entity", que é o valor textual reconhecido e "type", que é a classificação feita pela IA.

## Lista de Arquivos de Código Importantes

### financenews.py
Spider do Scrapy que recupera 5 notícias do site Finance News.
### scrapycaller.py
Classe que faz a integração entre o Scrapy e o resto da aplicação.
### entityfinder.py
Classe que utiliza o Spacy para reconhecer as entidades.
### api.py
API Flask, este é o arquivo que deve ser executado, ele fornece as rotas e faz uso do ScrapyCaller e do EntityFinder para ter acesso às funcionalidades do Scrapy e do Spacy.
