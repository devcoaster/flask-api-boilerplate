"""
Shared base classes for unit / int tests.
"""
from app.app import create_app
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
        config = {"DEBUG": 1}
        app_config = AppConfig(**config)
        self.app = create_app(app_config)
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
