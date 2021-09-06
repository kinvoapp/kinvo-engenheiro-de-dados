from flask import Flask

from kinvo.api.router import register_routes
from kinvo.core import config
from kinvo.logger import logger


def create_app():
    logger.info(f'Starting app')

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = config.SECRET_KEY

    # Initialize API routers
    register_routes(app)

    # Define a hello world page
    @app.route('/')
    def hello_world():
        return '<h1>Hello, World!</h1>'

    logger.info(f'App is up!')

    return app
