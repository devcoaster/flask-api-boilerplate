"""
Common utilities.
"""
from flask import Flask


def register_routes(app: Flask, routes: list) -> None:
    """
    Register routes on the provided flask app instance.
    """
    for route in routes:
        app.add_url_rule(
            **route
        )