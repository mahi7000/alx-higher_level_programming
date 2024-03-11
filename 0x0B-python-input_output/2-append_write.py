#!/usr/bin/python3
""" appends a string at the end of a text file (UTF8) """


def append_write(filename="", text=""):
    """ append text to filename """
    with open(filename, 'a', encoding='utf8') as file:
        file.write(text)
        return (len(text))
