from typing import Type

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.api import init_api_routes
from config import Config

api = Api()
db = SQLAlchemy()


def create_app(config: Type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    init_api_routes(api)
    api.init_app(app)

    return app


from app import models
