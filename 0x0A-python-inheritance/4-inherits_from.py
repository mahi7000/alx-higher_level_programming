#!/usr/bin/python3
""" subclass is it or not """


def inherits_from(obj, a_class):
    """ check if it is an instace of an inheritor """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
