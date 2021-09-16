#!/usr/bin/python3
def best_score(a_dictionary):
    bigger = 0
    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if v > bigger:
                bigger = v
        for k, v in a_dictionary.items():
            if v == bigger:
                return k
