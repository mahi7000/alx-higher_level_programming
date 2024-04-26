#!/usr/bin/python3
""" takes in a url and sends a request and displays alue """
from urllib import request
import sys

url = sys.argv[-1]

with request.urlopen(url) as response:
    request_id = response.getheader('X-Request-Id')

    print(request_id)
