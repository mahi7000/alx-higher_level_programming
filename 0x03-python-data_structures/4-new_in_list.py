#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    your_list = my_list[:]
    if (idx < 0):
        return (your_list)
    elif (idx >= len(your_list)):
        return (your_list)
    else:
        your_list[idx] = element
        return (your_list)

