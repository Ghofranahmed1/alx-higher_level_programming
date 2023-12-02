#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        rvs_list = my_list.reverse()
        for i in rvs_list:
            print("{:d}".format(i))
