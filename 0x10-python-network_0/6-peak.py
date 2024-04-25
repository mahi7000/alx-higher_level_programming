#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ finds peak """
    count = 1
    for i in list_of_integers[1:-1]:
        if list_of_integers[count - 1] <= i and\
            list_of_integers[count + 1] <= i:
                return i
        count += 1
