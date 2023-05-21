import unittest
from unittest.mock import patch, Mock
from md5hash import MD5Hash
import requests
from test.metabase_content import CONTENT


class TestMD5Hash(unittest.TestCase):
    def test_url_must_be_string(self):
        with self.assertRaises(TypeError):
            MD5Hash(123)

    @patch("requests.get")
    def test_successful_request_returns_md5_hash(self, mock_get):
        url = "https://www.metabase.com/images/favicon.ico"
        mock_response = Mock()
        mock_response.ok = True
        mock_response.content = CONTENT
        mock_get.return_value = mock_response
        expected_output = "4297c114f263c206ed12aaff4b0c7a50"

        md5_hash_object = MD5Hash(url)
        result = md5_hash_object.get_hash()

        self.assertEqual(result, expected_output)

    @patch("requests.get")
    def test_failed_request_returns_none(self, mock_get):
        url = "https://www.metabase.com/images/favicon.ico"
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        md5_hash_object = MD5Hash(url)
        result = md5_hash_object.get_hash()

        self.assertIsNone(result)

    @patch("requests.get", side_effect=requests.exceptions.RequestException())
    def test_exception_returns_none(self, mock_get):
        url = "https://www.metabase.com/images/favicon.ico"

        md5_hash_object = MD5Hash(url)
        result = md5_hash_object.get_hash()

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()