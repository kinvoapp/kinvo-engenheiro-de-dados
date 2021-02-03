from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return open('./web/index.html').read().replace("msg",'/minerar para minerar<br>/extrair para extrair')

@app.route('/minerar')
def minerarSalvar():
    return open('./web/index.html').read().replace("msg",'Minerando...')

@app.route('/extrair')
def extrairEntidades():
    return open('./web/index.html').read().replace("msg",'Extraindo...')