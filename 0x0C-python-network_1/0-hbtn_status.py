#!/usr/bin/python3
"""
A script that uses urllib to fetch/read the contents,
then prints type of the html variable and its content and
the utf8 content withing the variable
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))