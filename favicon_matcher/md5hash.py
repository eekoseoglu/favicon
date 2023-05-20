import hashlib
import requests
import sys

class MD5Hash:
    def __init__(self, url: str):
        if not isinstance(url, str):
            raise TypeError("URL must be a string")
        self.url = url

    def get_hash(self) -> str:
        try:
            response = requests.get(self.url)
            if response.ok:
                content = response.content
                md5_hash = hashlib.md5(content).hexdigest()
                return md5_hash
            else:
                print(f"Error: Request failed with status {response.status_code}", file=sys.stderr)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}", file=sys.stderr)
        
        return None
