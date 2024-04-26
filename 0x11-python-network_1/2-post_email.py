#!/usr/bin/python3
""" sends POST request """
from urllib import request, parse
import sys

url = sys.argv[-2]
email = sys.argv[-1]

data = parse.urlencode({'email': email}).encode()

with request.urlopen(url, data=data) as response:
    body = response.read().decode('utf-8')

    print("Your email is: {}".format(email))
