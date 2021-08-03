from flask import Flask
import os
from extrair import noticias 

app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'


@app.route('/get_news',methods=['GET'])
def createTask():
    os.system("scrapy runspider raspagem.py -o ../news/noticias_extraidas.csv")
    return "Noticias puxadas!"


@app.route('/get_entity',methods=['GET'])
def getTasks():

    return noticias().main()
    # return 'Get all named entity!'