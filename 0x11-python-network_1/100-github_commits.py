#!/usr/bin/python3
""" lists 10 commits """
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/"

    response = requests.get(url + owner + '/' + repo_name + '/commits').json()

    if response:
        for i in range(0, len(response)):
            print(response[i])
