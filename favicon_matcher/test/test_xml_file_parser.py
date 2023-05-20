import unittest
from unittest.mock import mock_open, patch
from xmltodict import parse
from xml_file_parser import XMLFileParser

class TestXMLFileParser(unittest.TestCase):
    
    def setUp(self):
        self.parser = XMLFileParser("favicons.xml")
    
    @patch("builtins.open", new_callable=mock_open, read_data="<root><name>John</name></root>")
    def test_parse_xml_to_dict(self, mock_file):
        expected_dict = parse("<root><name>John</name></root>")
        actual_dict = self.parser.parse_xml_to_dict()
        self.assertEqual(actual_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
