#!/usr/bin/python3
""" sends a request and displays body """
from urllib import request, error
import sys

url = sys.argv[-1]

try:
    with request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)

except error.HTTPError as e:
    print("Error code: {}".format(e.code))
