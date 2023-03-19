#!/usr/bin/python3
"""
takes GitHub username/password and uses GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username, token = argv[1:]

    s = requests.Session()

    data = {'username': username, 'token': token}
    response = s.get(url, auth=(username, token)).json()
    try:
        print(response['id'])
    except:
        print('None')
