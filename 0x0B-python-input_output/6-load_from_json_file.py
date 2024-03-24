#!/usr/bin/python3
""" creates an object from a json file """
import json


def load_from_json_file(filename):
    """ loads from json """
    with open(filename) as file:
        serialized_obj = file.read()
        return json.loads(serialized_obj)
