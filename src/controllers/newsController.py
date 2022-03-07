from flask import Flask
from flask_restx import Api, Resource

from src.server.server import server
from src.models.news import news


app, api = server.app, server.api


@api.route("/news")
class News(Resource):
    def post(self) -> int:
        try:
            news.obtain_news()
            return 200
        except Exception as e:
            return (f"Error: {e}", 415)

    def get(self) -> list:
        try:
            data = news.read_news()
            return (data, 200)
        except Exception as e:
            return (f"Error: {e}", 404)

