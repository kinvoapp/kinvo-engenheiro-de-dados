import crochet
import time

from flask import Blueprint, session, jsonify

from kinvo.database import crud
from kinvo.logger import logger
from kinvo.tasks import mining


newsbp = Blueprint("newsbp", __name__)


@newsbp.route('/crawl', methods=['POST'])
async def crawl():
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

    return {'message': "Data added to database successfully!"}, 202


@newsbp.route('/list', methods=['GET'])
def list_news():
    all_news = crud.get_news()
    all_news = [news.as_dict() for news in all_news]

    logger.info(f"Stored news: {all_news}")

    return jsonify(all_news), 200
