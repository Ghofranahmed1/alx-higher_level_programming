#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    Max = 0
    for k, v in a_dictionary.items():
        if v > Max:
            Max = v
    for k, v in a_dictionary.items():
        if v == Max:
            return k

