#!/usr/bin/python3
"""
takes URL as an argument, sends a request to the URL,
and displays the value of the X-Request-Id
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.info()
        x_id = header['X-Request-Id']

    print(x_id)
