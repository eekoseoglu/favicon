from fastapi import FastAPI
from md5hash import MD5Hash
from xml_file_parser import XMLFileParser
import socket

app = FastAPI()

@app.get("/my-first-api")
def hello(url: str):
    host_name = socket.gethostname()
    md5_hash_generator = MD5Hash(url)
    hash = md5_hash_generator.get_hash()
    my_parser = XMLFileParser("favicons.xml")
    my_dict = my_parser.parse_xml_to_dict()
    fingerprints = my_dict["fingerprints"]["fingerprint"]
    for fingerprint in fingerprints:
        if hash in fingerprint["example"]:
            return {host_name : 'This is my dict: ' + str(fingerprint["param"])} 
    return None



# docker build -t ekose/deneme:1.0 . --network=host
# docker run -p 8000:8000 ekose/hasher:1.1
# docker compose up -d
# docker-compose up --build --remove-orphans --scale app=3