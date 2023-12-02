#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    rvs_list = my_list[::-1]
    for i in rvs_list:
        print("{:d}".format(i))
