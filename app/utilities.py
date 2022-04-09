"""
Common utilities.
"""
import os
from flask import Flask
from dataclasses import dataclass
from dotenv import dotenv_values


@dataclass
class AppConfig:
    SQLALCHEMY_DATABASE_URI: str
    DEBUG: bool = False

    def __post_init__(self) -> None:
        """
        Validations for config values e.g database uri is correct etc.
        """
        pass


def load_raw_config() -> dict:
    """
    If env file is present, parse values from env file
    otherwise attempt to extract them from environment.
    """
    env_vals = dict(dotenv_values(".env"))
    if not env_vals:
        env_vals["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
        env_vals["DEBUG"] = os.getenv("DEBUG")

    return env_vals


def register_routes(app: Flask, routes: list) -> None:
    """
    Register routes on the provided flask app instance.
    """
    for route in routes:
        app.add_url_rule(**route)
