#!/usr/bin/python3
""" 3-to_json_string.py """
import json


def to_json_string(my_obj):
    """ convert python to json """
    return json.dumps(my_obj, sort_keys=True)
