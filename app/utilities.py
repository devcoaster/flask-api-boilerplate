"""
Common utilities.
"""
from flask import Flask
from dataclasses import dataclass


@dataclass
class AppConfig:
    DEBUG: bool = False

    def __post_init__(self) -> None:
        """
        Validations for config values e.g database uri is correct etc.
        """
        pass


def register_routes(app: Flask, routes: list) -> None:
    """
    Register routes on the provided flask app instance.
    """
    for route in routes:
        app.add_url_rule(**route)
