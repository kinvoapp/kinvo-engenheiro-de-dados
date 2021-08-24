from flask import Flask
from json import loads, dumps
from scrapycaller import ScrapyCaller
from entityfinder import EntityFinder

app = Flask(__name__)
caller = ScrapyCaller()
finder = EntityFinder()
pseudo_bd = []

@app.route('/get_scrapy', methods=['GET'])
def get_scrapy():
    global pseudo_bd
    output = caller.get_scrapy_output()
    pseudo_bd = loads(output)
    return output

@app.route('/get_spacy', methods=['GET'])
def get_spacy():
    global pseudo_bd
    if pseudo_bd:
        result = [(record['title'], finder.get_entities(record['title'])) for record in pseudo_bd]
        result = [{'text': data[0], 'entity_list': list(map(lambda ent: {'entity': ent.text, 'type': ent.label_}, data[1]))} for data in result]
        return dumps(result, ensure_ascii=False)
    else:
        return '[]'

if __name__ == '__main__':
    app.run()
