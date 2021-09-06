import crochet
from flask import current_app as app

from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher

from kinvo.logger import logger
from kinvo.database import crud
from kinvo.database import schemas
from kinvo.services.crawler import FinanceSpider


crochet.setup()


@crochet.run_in_reactor
def finance_news():
    dispatcher.connect(add_item, signal=signals.item_scraped)

    crawl_runner = CrawlerRunner()
    return crawl_runner.crawl(FinanceSpider)


def add_item(item, response, spider):
    try:
        news = schemas.NewsCreate(**item)
        logger.info(f"Add item: {news}")

        news = crud.create_news(news=news)
        logger.info(f"Data commited {news.id}")
    except Exception as e:
        logger.error(f"Something goes wrong: {e}")
