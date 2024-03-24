#!/usr/bin/python3
""" writes an objedt to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ saves file"""
    with open(filename, 'w') as file:
        serialized_obj = json.dumps(my_obj, sort_keys=True)
        file.write(serialized_obj)
