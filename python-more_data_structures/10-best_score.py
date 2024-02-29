#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    j = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            j = k
    return (j)
