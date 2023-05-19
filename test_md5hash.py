import unittest
import hashlib
import sys
from unittest.mock import patch
from md5hash import MD5Hash

class TestMD5Hash(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            MD5Hash(123)
        instance = MD5Hash('https://www.google.com')
        self.assertEqual(instance.url, 'https://www.google.com')

    @patch('requests.get')
    def test_fetch_content(self, mock_get):
        instance = MD5Hash('https://www.google.com')
        mock_get.return_value.content = b'test content'
        response = instance.fetch_content()
        mock_get.assert_called_once_with('https://www.google.com')
        self.assertEqual(response, b'test content')

    @patch('builtins.print')
    @patch('requests.get')
    def test_fetch_content_exception(self, mock_get, mock_print):
        instance = MD5Hash('https://www.google.com')
        mock_get.side_effect = Exception('Test Exception')
        response = instance.fetch_content()
        mock_get.assert_called_once_with('https://www.google.com')
        mock_print.assert_called_once_with('Error occured while fetching content: Test Exception', file=sys.stderr)
        self.assertIsNone(response)

    @patch.object(MD5Hash, 'fetch_content')
    def test_get_hash(self, mock_fetch_content):
        instance = MD5Hash('https://www.google.com')
        mock_fetch_content.return_value = b'test content'
        md5_hash = instance.get_hash()
        mock_fetch_content.assert_called_once()
        self.assertEqual(md5_hash, hashlib.md5(b'test content').hexdigest())

    @patch.object(MD5Hash, 'fetch_content')
    def test_get_hash_no_content(self, mock_fetch_content):
        instance = MD5Hash('https://www.google.com')
        mock_fetch_content.return_value = None
        md5_hash = instance.get_hash()
        mock_fetch_content.assert_called_once()
        self.assertIsNone(md5_hash)

if __name__ == '__main__':
    unittest.main()
