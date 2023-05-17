from  md5hash import MD5Hash
import sys

from fastapi import FastAPI

app = FastAPI()

@app.get("/my-first-api")
def hello(url: str):
    print(url)
    md5_hash_generator = MD5Hash(url)
    hash = md5_hash_generator.get_hash()
    return {'This is the hash: ' + hash} 


