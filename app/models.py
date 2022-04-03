"""
Models.
"""
from app.flask_extensions import db


class Greeting(db.Model):
    """
    Greeting model.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    language = db.Column(db.String(), nullable=False)
