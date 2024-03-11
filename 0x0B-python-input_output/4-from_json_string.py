#!/usr/bin/python3
""" returns an object from a json string """
import json


def from_json_string(my_str):
    """ from json to object """
    return json.loads(my_str)
