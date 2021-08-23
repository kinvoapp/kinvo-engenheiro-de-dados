from flask import Flask, render_template
from views import views
import requests
import json
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", )

@app.route("/mineirar", methods=['GET'])
def scrape():
    return views.mine_and_get()

@app.route("/processar", methods=['GET'])
def nlp():
    return views.nlp_api()  
        
@app.route("/front", methods=['GET'])
def front():
    response = requests.get('http://127.0.0.1:5000/processar', headers={"content-type":"application/json;charset=UTF-8"})
    data = response.json()
    return render_template("front.html", data = data)
        