from __future__ import unicode_literals
from flask import Flask, request, Response, render_template,session,redirect,url_for
from flask_restful import reqparse, abort, Api, Resource
import requests
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)
#mudar a porta scrapyrt -p 9000
@app.route('/')
#

def scrape():

	params = {
		'spider_name' :'finews',
		'start_request': True,
	}
	response=requests.get('http://localhost:9050/crawl.json',params)
	data = json.loads(response.text)
	df =pd.DataFrame(data=data, columns=['Title','Price','Stock','Star'])
	return render_template('base.html',  tables=[df.to_html(classes='data',  index=False)], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)

