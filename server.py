"""
Run app.
"""
from app.app import create_app
from app.utilities import AppConfig, load_raw_config


# Load raw config from .env file and load onto config dataclass for extra validation.
raw_config = load_raw_config()
app_config = AppConfig(**raw_config)

app = create_app(app_config)
