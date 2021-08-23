from flask import jsonify
import json
import requests
from nlp import nlp_processing

def mine_and_get():    
    params = {
        'spider_name' : 'news',
        'start_requests' : 'true'
    }
    
    response = requests.get('http://localhost:9080/crawl.json', params)
    data = json.loads(response.text)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data['items'],f, ensure_ascii=False, indent=4)
    return '<h1>Carregado!</h1>'

def nlp_api():
    return_dict = {"News" : []}
    processed_data = nlp_processing()
    if processed_data:
        for data in processed_data:
            return_dict['News'].append(data)
        return jsonify({'data' : return_dict})
    return '<h1>Não existem notícias para serem processadas!</h1>'