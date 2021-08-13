import json
from flask.json import jsonify
from flask import Flask
import subprocess

app = Flask(__name__)

app.secret_key = "kinvioIA"

@app.route('/api/v1/feed', methods=['GET', 'POST'])
def feed():
    with open('outputfile.json') as f:
        feeds = json.load(f)
        n = [a for a in feeds]
        resp = jsonify(n)

    return resp

@app.route('/api/v1/extract', methods=['GET', 'POST'])
def input():
    pass1 = subprocess.call('del outputfile.json', shell=True)
    pass2 = subprocess.call('scrapy runspider scraper.py -t json -o outputfile.json', shell=True)

    m = {'message': 'Feeds extraídos com sucesso.'}
    resp = jsonify(m)

    return resp

if __name__ == "__main__":
    app.run(debug=True)