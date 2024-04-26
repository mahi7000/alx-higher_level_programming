#!/usr/bin/python3
""" displays id after taking github info """
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    user_id = response.json().get('id')
    print(user_id)
