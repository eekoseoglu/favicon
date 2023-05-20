import xmltodict

class XMLFileParser:
    def __init__(self, filename: str):
        self.filename = filename
    
    def parse_xml_to_dict(self) -> dict:
        with open(self.filename, "r") as fileptr:
            my_dict = xmltodict.parse(fileptr.read())
        return my_dict
