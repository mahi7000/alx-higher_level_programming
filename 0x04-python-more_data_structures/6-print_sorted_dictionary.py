#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorti = dict(sorted(a_dictionary))
    for item in sorti:
        print("{}: {}".format(item, sorti[item]))
