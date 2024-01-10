#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    dset_1 = set_1.difference(set_2)
    dset_2 = set_2.difference(set_1)
    uni_d = dset_1.union(dset_2)
    return (uni_d)
