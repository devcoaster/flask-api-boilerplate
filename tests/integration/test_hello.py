"""
Integration tests for hello route.
"""
from tests.common import IntegrationBaseTest


class TestHello(IntegrationBaseTest):
    """
    Test hello view.
    """

    def test_get(self) -> None:
        """
        GET request should retrieve greetings in the database.
        """
        resp = self.test_client.get("/hello")

        resp_json = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_json, {"message": "Success", "data": []})

    def test_post(self) -> None:
        """
        Post request with valid greeting should save new entry.
        """
        payload = {"name": "Habari", "language": "Swahili"}
        resp = self.test_client.post("/hello", json=payload)

        resp_json = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp_json,
            {
                "message": "Successfully added new greeting",
                "greeting": {"id": 1, "name": "Habari", "language": "Swahili"},
            },
        )

    def test_post_validations(self) -> None:
        """
        If fields are missing, response should be an error.
        """
        payload = {"name": "Habari"}
        resp = self.test_client.post("/hello", json=payload)

        resp_json = resp.get_json()
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp_json, {"error": "Missing name or language"})
