#!/usr/bin/python3
""" takes in a letter and sends POST request """
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data={'q': q})

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'),
                data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
