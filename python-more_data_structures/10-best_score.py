#!/usr/bin/python3
def best_score(a_dictionary):
  if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    j = list(a_dictionary.keys())[0]
    big = a_dictionary[j]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            j = k
    return (j)
