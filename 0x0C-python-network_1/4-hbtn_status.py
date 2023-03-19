#!/usr/bin/python3
"""
a script that uses the requests library to fetch
the status of a URL, then prints the type and content
from the request
"""
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
