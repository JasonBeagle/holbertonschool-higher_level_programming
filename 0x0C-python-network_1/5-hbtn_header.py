#!/usr/bin/python3
"""
script using requests module to make a
request to a URL, then prints the value of the X-Request-Id header
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
