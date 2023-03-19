#!/usr/bin/python3
"""
a script that uses the requests library to fetch
the status of a URL, then prints the type and content
from the request
"""
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)

    content = response.content.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
