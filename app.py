from flask import Flask
app = Flask(__name__)

# hello world basico
@app.route("/")
def home():
    return "Hello World!"

# route para o crawler
@app.route("/crawler")
def crawler():
    file = open('kinvo-ia-test\\b3StockNews\\b3stocks.py', 'r').read()
    return exec(file)

# route para a nlp
@app.route("/extractor")
def extractor():
    file = open('kinvo-ia-test\\nlp.py').read()
    return exec(file)
