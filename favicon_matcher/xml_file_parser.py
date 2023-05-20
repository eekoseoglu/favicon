import xmltodict


class XMLFileParser:
    def __init__(self, filename: str):
        self.filename = filename

    def parse_xml_to_dict(self) -> dict:
        with open(self.filename, "r") as file_ptr:
            my_dict = xmltodict.parse(file_ptr.read())
        return my_dict
