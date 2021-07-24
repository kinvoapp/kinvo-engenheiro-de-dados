import os
import subprocess
import requests
import re
import spacy
from datetime import datetime
from flask import Flask, request
from bs4 import BeautifulSoup

app = Flask(__name__)

false_entities = ["R$","”"]

# Cria diretório
os.makedirs("noticias", exist_ok=True)

# O flask vai demorar pra subir, pois demora pra carregar o Spacy. Melhor carregar aqui do que a cada requisição no endpoint.
nlp = spacy.load("pt_core_news_sm")

# Vai executar o scrapy para buscar 5 notícias do feed do financenews, no html salvo pelo scrapy
# Vai executar no background, em outra Thread
@app.route("/getNews")
def get_news():
    try:

        # Executa o projeto do scrapy
        subprocess.check_output(['scrapy', 'crawl', 'crawler'])

        # Após gerar o HTML, busca tags nele que levem à notícias relacionadas à b3
        if os.path.isfile('news-financenews.html'):

            with open('news-financenews.html', 'r', encoding="utf8") as f:
                contents = f.read()
                soup = BeautifulSoup(contents, 'lxml')
                noticia = 1

                for link in soup.find_all('link'):
                    if noticia == 6:
                        return f"<h1>Crawler executado. {datetime.now()}</h1>"

                    if link.next is not None:
                        content = requests.get(link.next.replace("\t", "").replace("\n", ""))

                        soup2 = BeautifulSoup(content.text, 'html.parser')

                        div_title = soup2.find('div', {"class": "title-single"})

                        if div_title is not None:
                            div_post = soup2.find('div', {"class": "page-post"})
                            if div_post is not None:
                                with open('noticias/noticia-' + str(noticia) + '.txt', 'w',
                                          encoding="UTF-8") as f2:
                                    f2.write(str(div_title.text) + str(div_post.text))
                                noticia += 1
        return f"<h1>Crawler executado. {datetime.now()}</h1>"
    except Exception as e:
        return f"<h1>Erro: {e} </h1>"


# Realiza entity recognition nas notícias baixadas
@app.route("/processNews")
def process_news():
    try:
        output = dict()

        for filename in os.listdir('noticias'):

            with open('noticias/' + filename, 'r', encoding="UTF-8") as f:
                entities_listed = list()
                output[filename] = {
                    "title": "",
                    "entities": list()
                }

                content = f.read()
                # Retira espaços do HTML
                content = content.replace("NBSP", "")
                # Retira links
                content = re.sub(r'^https?:\/\/.*[\r\n]*', '', content, flags=re.MULTILINE)

                doc = nlp(content)
                for ent in doc.ents:
                    if ent.text.strip() != "" and ent.text != "R$" and len(ent.text) > 2 and ent.text not in entities_listed:
                        output[filename]["title"] = content.split("\n")[1]
                        output[filename]["entities"].append([ent.text, ent.label_])
                        entities_listed.append(ent.text)

        response = ''
        # Gera saída em HTML
        for key in output:
            response += f"<h1>{output[key]['title']}</h1><table><thead><th>Entity</th><th>Label</th></thead><tbody>"
            for entity in output[key]["entities"]:
                response += f"<tr><td>{entity[0]}</td><td>{entity[1]}</td></tr>"
            response += "</tbody></table><hr/>"

        if len(output) == 0:
            return "<h1>Nenhuma notícia foi processada</h1>"
        else:
            return response
    except Exception as e:
        return f"<h1>Erro: {e} </h1>"


if __name__ == '__main__':
    app.run()
