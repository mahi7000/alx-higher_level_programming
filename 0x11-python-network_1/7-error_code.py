#!/usr/bin/python3
""" request url and displays body """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[-1]

    response = requests.get(url)
    body = response.text

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(body)
