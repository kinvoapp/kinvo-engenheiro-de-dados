from flask import Flask,render_template
import pandas as pd 
import json
import os
import spacy

app = Flask("Minerando")

@app.route('/getnews')
def getnews():
    
    if not os.path.exists('news.json'):
        os.system("scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 spiders/spiders/spiders/Myspider.py -o news.json")
        

    if os.path.exists('news.json'):
        arq = pd.read_json('news.json',encoding='utf8')
        data = arq[['title','news']].head(5).to_dict(orient='records')

        return render_template('index.html', data=data)


@app.route('/getentity')
def getentity():
    try:
        nlp = spacy.load("pt_core_news_sm")

        with open('news.json','r') as file:
            news = json.loads(file.read())
            output = list()

        for new in news:
            #convertendo de dicionario pra string
            new = str(new)
            doc = nlp(new)
            entidades = []

            #encontrando entidades nomeadas, frases e conceitos.
            for entity in doc.ents:
                entidades.append({
                    "trexo":entity.text,
                    "entidade":entity.label_
                })
                output = entidades
                
        return render_template('scapy.html',data=output)  
    except IOError:
        return  '<h1>Erro ao obter entidade, execute o endpoint /getnews para obter as noticias antes.</h1>'

if __name__ == '__main__':
    app.run(debug=True)