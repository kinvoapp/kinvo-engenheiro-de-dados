----------*----------*----------*----------*----------*----------*----------*----------*----------*
Dado ao meu começo de aprendizagem a linguagem Python, somente consegui efetuar a primeira parte
que é a mineração das notícias, obtendo seu título, descrição e link.

Gostaria de receber posteriormente o gabarito deste exercício para que eu possa estudá-lo. 
Obrigado pela oportunidade!
----------*----------*----------*----------*----------*----------*----------*----------*----------*

No terminal do pycharm foram utilizados os seguintes comandos para a realização da mineração dos dados da página do G1:
scrapy genspider FinSpider https://g1.globo.com/
Para que seja gerado o script de spider


E foi utilizado o comando:
scrapy runspider FinSpider.py --nolog -o noticias.json
Para que seja salvo os dados consultados no arquivo noticias.json







