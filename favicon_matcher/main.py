# from fastapi import FastAPI
# from md5hash import MD5Hash
# from xml_file_parser import XMLFileParser
# import socket


# app = FastAPI()


# @app.get("/my-first-api")
# def hello(url: str):
#     host_name = socket.gethostname()
#     md5_hash_generator = MD5Hash(url)
#     hash_value = md5_hash_generator.get_hash()

#     my_parser = XMLFileParser("favicons.xml")
#     my_dict = my_parser.parse_xml_to_dict()

#     fingerprints = my_dict["fingerprints"]["fingerprint"]
#     for fingerprint in fingerprints:
#         if hash_value in fingerprint["example"]:
#             return {host_name: 'This is my dict: ' + str(fingerprint["param"])}

#     return None


from fastapi import FastAPI
from md5hash import MD5Hash
from xml_file_parser import XMLFileParser
import socket


app = FastAPI()

# Parse favicons.xml once and cache it.
my_parser = XMLFileParser("favicons.xml")
my_dict = my_parser.parse_xml_to_dict()

# Store the fingerprints examples in a set
fingerprints = set(fingerprint["example"] for fingerprint in my_dict["fingerprints"]["fingerprint"])


@app.get("/my-first-api")
def hello(url: str):
    host_name = socket.gethostname()
    md5_hash_generator = MD5Hash(url)
    hash_value = md5_hash_generator.get_hash()

    if hash_value in fingerprints:
        for fingerprint in my_dict["fingerprints"]["fingerprint"]:
            if hash_value == fingerprint["example"]:
                return {host_name: f'This is my dict: {fingerprint["param"]}'}

    return None
