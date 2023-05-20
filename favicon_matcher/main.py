from fastapi import FastAPI
from md5hash import MD5Hash
from xml_file_parser import XMLFileParser
import socket


app = FastAPI()


@app.get("/my-first-api")
def hello(url: str):
    host_name = socket.gethostname()
    md5_hash_generator = MD5Hash(url)
    hash_value = md5_hash_generator.get_hash()

    my_parser = XMLFileParser("favicons.xml")
    my_dict = my_parser.parse_xml_to_dict()

    fingerprints = my_dict["fingerprints"]["fingerprint"]
    for fingerprint in fingerprints:
        if hash_value in fingerprint["example"]:
            return {host_name: 'This is my dict: ' + str(fingerprint["param"])}

    return None
