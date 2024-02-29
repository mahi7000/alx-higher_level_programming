#!/usr/bin/python3

def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None

    scoreb = int(map(lambda x, y: x > y, a_dictionary))
    return (scoreb)
