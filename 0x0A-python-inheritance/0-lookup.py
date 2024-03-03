#!/usr/bin/python3
""" lists available attributes and methods of an object """


def lookup(obj):
    """ lists the available attrivutes """
    dir_list = dir(obj)
    return (dir_list)
