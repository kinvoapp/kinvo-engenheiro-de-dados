from flask import Flask, render_template
from webcrawlear import WebCrawlear

app = Flask(__name__)
dicionario = {'lista_news': ['Lista ainda não foi carregada. [Para carregar utilize endpoint "/savenews"]']}

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/topnews')
def topnews():
    return render_template('news.html', items=dicionario['lista_news'][:5]);

@app.route('/news')
def news():
    return render_template('news.html', items=dicionario['lista_news']);

@app.route('/savenews')
def savenews():
    webscrawlear = WebCrawlear()
    dicionario['lista_news'] = webscrawlear.main()
    return render_template('savenews.html');

app.run()