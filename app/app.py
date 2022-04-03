"""
App creation with app factory pattern.
"""
from flask import Flask
from app.routes import routes
from app.utilities import register_routes


def create_app(config: dict = {}):
    """
    Create flask app configured with provided config.
    """
    app = Flask(__name__.split(".")[0])

    app.config.from_object(config)

    register_routes(app, routes)

    return app
