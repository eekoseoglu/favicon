import os
import tempfile
import unittest
from xml.parsers.expat import ExpatError
from xml_file_parser import XMLFileParser


class TestXMLFileParser(unittest.TestCase):

    def setUp(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"<root><emre>12345</emre></root>")
            self.filename = temp_file.name

    def tearDown(self):
        os.unlink(self.filename)

    def test_parse_xml_to_dict_returns_dict(self):
        parser = XMLFileParser(self.filename)
        result = parser.parse_xml_to_dict()
        self.assertIsInstance(result, dict)

    def test_parse_xml_to_dict_returns_correct_dict_structure(self):
        parser = XMLFileParser(self.filename)
        result = parser.parse_xml_to_dict()
        expected_result = {"root": {"emre": "12345"}}
        self.assertEqual(result, expected_result)

    def test_parse_xml_to_dict_handles_invalid_xml(self):
        with open(self.filename, 'w') as file_ptr:
            file_ptr.write('<root><test> 12345 </root>')  # invalid XML - missing closing tag

        parser = XMLFileParser(self.filename)

        with self.assertRaises(ExpatError): 
            parser.parse_xml_to_dict()


if __name__ == '__main__':
    unittest.main()
