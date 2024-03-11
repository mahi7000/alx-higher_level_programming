#!/usr/bin/python3
""" writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """ write a text in filename """
    with open(filename, 'w', encoding='utf8') as file:
        file.write(text)
        return (len(text))
