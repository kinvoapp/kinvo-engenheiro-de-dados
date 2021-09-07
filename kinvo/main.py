import spacy

from flask import Flask

from kinvo.api import routesbp
from kinvo.core import config
from kinvo.logger import logger


def create_app():
    logger.info(f'Starting app')

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = config.SECRET_KEY

    app.nlp_model = spacy.load("pt_core_news_sm")

    # Initialize API routers
    app.register_blueprint(routesbp, url_prefix=config.API_PREFIX)

    # Define a hello world page
    @ app.route('/')
    def hello_world():
        return '<h1>Hello, World!</h1>'

    logger.info(f'App is ready!')

    return app
