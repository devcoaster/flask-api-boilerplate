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
        Get request to hello should return successful response.
        """
        resp = self.test_client.get("/hello")

        resp_json = resp.get_json()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_json, {"message": "Hello"})

    def test_post(self) -> None:
        """
        Post request with a name returns the name as part of greeting.
        """
        test_cases = [
            ("Name present in json payload", {"name": "teapot"}, "Hello teapot!"),
            ("Name not in json payload", {}, "Hello anonymous!"),
        ]

        for _, payload, expected_resp in test_cases:
            resp = self.test_client.post("/hello", json=payload)

            resp_json = resp.get_json()
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp_json, {"message": expected_resp})
