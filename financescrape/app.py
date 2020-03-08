from klein import  Klein
import json
from financescrape.spider_runner import  SpiderRunner
from financescrape.utils import return_spider_output, save_finance_json, save_b3_csv, get_finance
from financescrape.spiders import b3, financenews, ultimoinstate
import spacy

# Instructions
# 1- Before running the api/ endpoints, make sure there is a b3.csv file in the files folder.
# 1.1 - If there isn't a b3.csv, run the get_b3 endpoint first.
# 2- Before running the api/extract_entities endpoint, make sure there is a finance.jsonl file in the files folder.
# 2.2 - If there isn't a finance.jsonl file, run the api/mine_save endpoint first.
# 3- To run the tests, run it from outside the tests folder
# 3.1 Example: python -m unittest tests/test_spider.py


app = Klein()
nlp = spacy.load("pt_core_news_sm")

@app.route('/api/mine_save')
def mine_save(request):
    """
    Mine and save the news from financenews and ultimoinstante.
    """
    try:
        runner = SpiderRunner()

        deferred = runner.crawl(financenews.FinanceNews)
        deferred.addCallback(save_finance_json)


        deferred = runner.crawl(ultimoinstate.UltimoInstante)
        deferred.addCallback(save_finance_json)

        return "OK"

    except Exception as error:
        return "Error: "+str(error)


@app.route('/api/extract_entities/<int:num>')
def extract_entities(request, num):
    """
    Extract the entities of the last <int:num> news and return the info.
    """
    analyzed = []
    news = get_finance(num)
    for new in news:
        ent_list = []
        entities = nlp(dict(new)['title'])
        for ent in entities.ents:
            ent_list.append(ent.text)
        analyzed.append({'origin':new['origin'], 'title': new['title'], 'entities': ent_list})

    return json.dumps(analyzed)


@app.route('/get_b3')
def get_B3(request):
    """
    Get B3 info from https://br.advfn.com/bolsa-de-valores/bovespa and save it into a csv file
    """
    runner = SpiderRunner()

    deferred = runner.crawl(b3.B3)
    deferred.addCallback(save_b3_csv)
    deferred.addCallback(return_spider_output)

    return deferred



if __name__ == "__main__":
    app.run("localhost", 8080)