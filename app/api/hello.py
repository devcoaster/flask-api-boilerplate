"""
Sample method view.
"""
from flask import Response, jsonify, request
from app.api.base import BaseMethodView
from app.flask_extensions import db
from app.models import Greeting


class Hello(BaseMethodView):
    """
    Sample view.
    """

    def get(self) -> Response:
        """
        Handle GET request method.
        """
        greetings = [i.to_dict() for i in Greeting.query.limit(20)]
        resp_data = {"data": greetings, "message": "Success"}
        return jsonify(resp_data)

    def post(self) -> Response:
        """
        POST request method.
        """
        req_payload = request.get_json()
        name = req_payload.get("name")
        language = req_payload.get("language")
        if not language or not name:
            return jsonify({"error": f"Missing name or language"}), 400

        exist_check = Greeting.query.filter(
            (Greeting.name == name) | (Greeting.language == language)
        ).first()
        if exist_check:
            return (
                jsonify({"error": f"{language} greeting {name} already exists!"}),
                400,
            )

        new_greeting = Greeting(name=str(name), language=str(language))
        db.session.add(new_greeting)
        db.session.commit()
        resp_data = {
            "message": "Successfully added new greeting",
            "greeting": new_greeting.to_dict(),
        }

        return jsonify(resp_data)
