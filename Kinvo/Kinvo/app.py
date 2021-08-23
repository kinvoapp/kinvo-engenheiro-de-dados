import os
from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "feedspider.json")
    data = json.load(open(json_url))
    return render_template('index.html', data=data)