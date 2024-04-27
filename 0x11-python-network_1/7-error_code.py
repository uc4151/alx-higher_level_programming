#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    reqst = requests.get(url)

    if reqst.status_code >= 400:
        print("Error code: {}".format(reqst.status_code))
    else:
        print(reqst.text)
