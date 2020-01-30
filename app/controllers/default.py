from flask import render_template
from app import app

@app.route("/home")
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/minerar")
def minerar():
    return render_template('mining.html')

@app.route("/extrair")
def extrair():
    return render_template('extraction.html')

#@app.route("/test")
#def test():
#    return render_template('test.html')
