#!/usr/bin/python3
""" class inherits from list """


class MyList(list):
    """ class that accepts a list """
    def print_sorted(self):
        """ prints out sorted list """
        sorted_list = sorted(self)
        print(sorted_list)
