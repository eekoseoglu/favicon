import xmltodict

class XMLFileParser:
    def __init__(self, filename):
        self.filename = filename
    
    def parse_xml_to_dict(self):
        with open(self.filename, "r") as fileptr:
            xml_content = fileptr.read()
            my_dict = xmltodict.parse(xml_content)
        return my_dict
