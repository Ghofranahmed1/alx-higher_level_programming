#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    range_limit = len(my_list) - 1
    if (idx < 0 or idx > range_limit):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
