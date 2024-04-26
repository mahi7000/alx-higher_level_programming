#!/usr/bin/python3
""" send POST request with email as parameter """
import requests
import sys

url = sys.argv[-2]
email = sys.argv[-1]

data = {'email': email}

response = requests.post(url, data=data)

print("Your email is: {}".format(email))
