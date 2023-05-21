from fastapi import FastAPI
import favicon
from md5hash import MD5Hash
from xml_file_parser import XMLFileParser

app = FastAPI()
xml_parser = XMLFileParser("favicons.xml")
big_dict = xml_parser.parse_xml_to_dict()

hash_dict = {}

for fingerprint in big_dict["fingerprints"]["fingerprint"]:
    example_hash = fingerprint["example"]
    if isinstance(example_hash, list):
        for hash_value in example_hash:
            hash_dict[hash_value] = fingerprint["param"]
    elif isinstance(example_hash, str):
        hash_dict[example_hash] = fingerprint["param"]


@app.get("/my-first-api")
def get_properties(url: str):
    icons = favicon.get(url)

    for icon in icons:
        if "favicon.ico" in icon.url:
            md5_hash_generator = MD5Hash(icon.url)
            hash_value = md5_hash_generator.get_hash()
            return hash_dict.get(hash_value, None)
    return None
