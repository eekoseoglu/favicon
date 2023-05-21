import os
import unittest
import tempfile
from xml.etree import ElementTree as ET


class TestXMLFileParser(unittest.TestCase):
    def setUp(self):
        self.xml_data = "<root><emre>12345</emre></root>"
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(self.xml_data.encode())
        self.temp_file.close()

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_parse_xml_to_dict(self):
        expected_dict = {'emre': '12345'}
        tree = ET.parse(self.temp_file.name)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        self.assertEqual(result, expected_dict)


if __name__ == '__main__':
    unittest.main()
