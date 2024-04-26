#!/usr/bin/python3
""" takes in a url and sends a request and displays alue """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[-1]

    with urllib.request.urlopen(url) as response:
        request_id = info()['X-Request-Id']

        print(request_id)
