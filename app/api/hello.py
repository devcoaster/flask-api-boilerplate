"""
Sample method view.
"""
from flask import Response, jsonify, request
from app.api.base import BaseMethodView


class Hello(BaseMethodView):
    """
    Sample view.
    """

    def get(self) -> Response:
        """
        Handle GET request method.
        """
        resp_data = {"message": "Hello"}

        return jsonify(resp_data)

    def post(self) -> Response:
        """
        POST request method.
        """
        req_payload = request.get_json()
        resp_data = {"message": f"Hello {req_payload.get('name', 'anonymous')}!"}

        return jsonify(resp_data)
