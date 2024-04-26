#!/usr/bin/python3
""" sends POST request """
import urllib.request
import urllib.parse
import sys

url = sys.argv[-2]
email = sys.argv[-1]

data = urllib.parse.urlencode({'email': email}).encode()

with urllibrequest.urlopen(url, data=data) as response:
    body = response.read().decode('utf-8')

    print("Your email is: {}".format(email))
