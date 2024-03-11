#!/usr/bin/python3
""" eads a text file (UTF8) """


def read_file(filename=""):
    """ reads file """
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            print(line, end='')
