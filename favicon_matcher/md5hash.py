import hashlib
import sys
import requests

class MD5Hash:
    def __init__(self, url):
        if not isinstance(url, str):
            raise TypeError("URL must be a string")
        self.url = url

    def fetch_content(self):
        try:
            response = requests.get(self.url)
            return response.content
        except Exception as e:
            print(f"Error occured while fetching content: {e}", file=sys.stderr)
            return None
        
    def get_hash(self):
        content = self.fetch_content()
        if content:
            md5_hash = hashlib.md5(content).hexdigest()
            return md5_hash
        else:
            return None
        