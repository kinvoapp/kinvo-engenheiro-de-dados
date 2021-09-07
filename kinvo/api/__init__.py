import crochet
import time

from flask import Blueprint, session, jsonify, current_app

from kinvo.tasks import mining
from kinvo.logger import logger
from kinvo.database import crud


routesbp = Blueprint("routesbp", __name__)


@routesbp.route('/entities', methods=['GET'])
def entities():
    all_news = crud.get_news()

    response = []

    for news in all_news:
        entities = current_app.nlp_model(news.content).ents
        entities = {"entities": [{'entity': e.text, 'label': e.label_}
                    for e in entities]}

        response.append({**news.as_dict(), **entities})

    logger.info(f"Entites response: {response}")

    return jsonify(response), 200


@routesbp.route('/news', methods=['POST'])
def news():
    if 'crawl' not in session:
        task = mining.finance_news()
        session['crawl'] = task.stash()

        logger.info("Crawl data")
        time.sleep(10)

    r = crochet.retrieve_result(session.pop('crawl'))

    try:
        r.wait(timeout=None)
        logger.info(f"Finished Crawl")
    except crochet.TimeoutError:
        session['crawl'] = r.stash()
        logger.info("In progress...")
    except:
        logger.error(("Crawl failed:\n "
                      f"{r.original_failure().getTraceback()}"))

    all_news = crud.get_news()
    all_news = [news.as_dict() for news in all_news]

    logger.info(f"Response news ({len(all_news)}): {all_news}")

    return jsonify(all_news), 202
