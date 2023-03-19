#!/usr/bin/python3
"""
a script that takes an email, sends a POST request to the URL
with the email as a param, and displays the body of the response
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
