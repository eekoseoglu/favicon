import unittest
from fastapi.testclient import TestClient
from main import app

class TestMyFirstAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_hello_with_existing_hash(self):
        url = "https://jellyfin.org/images/favicon.ico"
        response = self.client.get("/my-first-api", params={"url": url})
        expected_param = [{"@pos":"0","@name":"service.vendor","@value":"Jellyfin"},{"@pos":"0","@name":"service.product","@value":"Media Server"}]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_param)

    def test_hello_with_nonexistent_hash(self):
        url = "https://www.google.com/"
        response = self.client.get("/my-first-api", params={"url": url})
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.json())

if __name__ == "__main__":
    unittest.main()