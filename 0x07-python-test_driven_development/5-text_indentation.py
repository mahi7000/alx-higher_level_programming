#!/usr/bin/python3
""" prints a text with 2 new lines
    after each of these characters: ., ? and : """


def text_indentation(text):
    """ prints a text with 2 new lines after  ., ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for letter in text:
        if flag == 0:
            if letter == ' ':
                continue
            else:
                flag = 1

        if flag == 1:
            if letter == '.' or letter == ':' or letter == '?':
                print(letter + '\n')
                flag = 0
            else:
                print(letter, end='')
