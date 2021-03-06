"""
App creation with app factory pattern.
"""
from flask import Flask
from app.flask_extensions import db, migrate
from app.routes import routes
from app.utilities import AppConfig, register_routes


def create_app(config: AppConfig):
    """
    Create flask app configured with provided config.
    """
    app = Flask(__name__.split(".")[0])

    app.config.from_object(config)

    # Attach extensions to flask app inst.
    db.init_app(app)
    migrate.init_app(app, db)

    register_routes(app, routes)

    return app
