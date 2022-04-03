"""
Shared base classes for unit / int tests.
"""
from app.app import create_app
from app.flask_extensions import db
from app.utilities import AppConfig

from unittest import TestCase


class IntegrationBaseTest(TestCase):
    """
    Common logic for int tests - setting up test app.
    """

    def setUp(self) -> None:
        """
        Create app and test client.
        """
        super().setUp()
        # Add testing config here.
        config = {"DEBUG": 1, "SQLALCHEMY_DATABASE_URI": "sqlite://"}
        app_config = AppConfig(**config)
        self.app = create_app(app_config)

        # Create tables in in memory db for testing.
        with self.app.app_context():
            db.create_all()

        self.test_client = self.app.test_client()


class UnitBaseTest(TestCase):
    """
    Common logic for unit tests.
    """

    def setUp(self) -> None:
        """
        Common.
        """
        super().setUp()
