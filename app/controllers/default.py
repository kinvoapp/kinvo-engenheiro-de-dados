from flask import render_template
from app import app
import subprocess
import numpy as np
import spacy
import pandas as pd
import json

@app.route("/home")
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/minerar")
def minerar():
    try:
        with open('news.json', 'r') as file:
            dados_noticias = json.load(file)
            df=pd.DataFrame(data=dados_noticias, columns=['Data','Titulo','Noticia'])

    except IOError:
        print ('Arquivo não encontrado! start mining')
        spider_name = "notices"
        subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", "news.json"])
        with open('news.json', 'r') as file:
            dados_noticias = json.load(file)
            df=pd.DataFrame(data=dados_noticias, columns=['Data','Titulo','Noticia'])

    return render_template('mining.html', tables=[df.to_html(classes='table table-dark',  index=False, justify='center', max_rows=6)])

@app.route("/extrair")
def extrair():
    with open('news.json', 'r') as file:
        dados_noticias = json.load(file)
        df=pd.DataFrame(data=dados_noticias, columns=['Data','Titulo','Noticia'])
        nlp = spacy.load("pt_core_news_sm")
        nlp2 = spacy.load("model_lucas")
        noticias_selecionadas=df.head()
        palavras_chave=[]
        categoria_chave=[]
        palavras_chave2=[]
        categoria_chave2=[]
        for new in noticias_selecionadas['Noticia']:
            doc=nlp(new)
            doc2=nlp2(new)
            palavras_chave.append([p.text for p in doc.ents])
            categoria_chave.append([p.label_ for p in doc.ents])
            palavras_chave2.append([p.text for p in doc2.ents])
            categoria_chave2.append([p.label_ for p in doc2.ents])
        dados_tratados={'Palavras detectadas':palavras_chave,'Entidade reconhecida':categoria_chave}
        dados_tratados2={'Palavras detectadas':palavras_chave2,'Entidade reconhecida':categoria_chave2}
        df2=pd.DataFrame(data=dados_tratados, index=noticias_selecionadas['Noticia'])
        df3=pd.DataFrame(data=dados_tratados2, index=noticias_selecionadas['Noticia'])

    return render_template('extraction.html', tables1=[df2.to_html(classes='table table-dark', justify='center', max_rows=6)],tables2=[df3.to_html(classes='table table-dark', justify='center', max_rows=6)])
