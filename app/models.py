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

    def to_dict(self) -> dict:
        """
        Obj to dict.
        """
        return {"id": self.id, "name": self.name, "language": self.language}
