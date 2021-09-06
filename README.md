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


3. Após terminar seu teste submeta um pull request e aguarde seu feedback.


### Pré-requisitos:

* Utilizar Flask;
* Utilizar Python;
* Utilizar Spacy;
* Utilizar Scrapy;


**Importante:** Usamos o mesmo teste para todos os níveis de desenvolvedor, **junior**, **pleno** ou **senior**, mas procuramos adequar nossa exigência na avaliação com cada um desses níveis sem, por exemplo, exigir excelência de quem está começando :-)

## Submissão

Para iniciar o teste, faça um fork deste repositório, crie uma branch com o seu nome e depois envie-nos o pull request.
Se você apenas clonar o repositório não vai conseguir fazer push e depois vai ser mais complicado fazer o pull request.

**Sucesso!**

# Executando a aplicação

## Pré-requisitos
- [Python 3.^](https://www.python.org)
- [Docker](https://www.docker.com)
- [Ubuntu 20.04.2 LTS](https://ubuntu.com)

## Descrição
A aplicação consiste em uma API rest feita em **Flask** que faz a mineração de noticiais sobre a empresa B3 dos sites [Finance news](https://financenews.com.br) e [Ultimo instante](https://www.ultimoinstante.com.br).

## Instruções de execução
Para executar bastar dar permissão ao arquivo `start.sh`:
```bash
chmod 777 start.sh
```
E Startar a aplicação basta executar o seguinte comando:
```bash
./start.sh
```
