"""
Run app.
"""
from dotenv import dotenv_values
from app.app import create_app
from app.utilities import AppConfig


# Load raw config from .env file and load onto config dataclass for extra validation.
raw_config = dict(dotenv_values(".env"))
app_config = AppConfig(**raw_config)

app = create_app(app_config)
