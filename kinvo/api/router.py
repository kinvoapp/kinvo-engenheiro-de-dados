from kinvo.core import config

from .routes.entities import entitybp
from .routes.heatbeat import heartbp
from .routes.news import newsbp


def register_routes(app):
    app.register_blueprint(entitybp, url_prefix=f'{config.API_PREFIX}/entities')
    app.register_blueprint(heartbp, url_prefix=f'{config.API_PREFIX}/health')
    app.register_blueprint(newsbp, url_prefix=f'{config.API_PREFIX}/news')
