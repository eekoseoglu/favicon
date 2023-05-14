#!/usr/bin/env python3

import hashlib
import sys
import requests

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} [Favicon URL]")
    sys.exit(0)

try:
    response = requests.get(sys.argv[1])
    md5_hash = hashlib.md5(response.content).hexdigest()
    print(md5_hash)

except Exception as e:
    print(f"Error occured as: {e}", file=sys.stderr)
