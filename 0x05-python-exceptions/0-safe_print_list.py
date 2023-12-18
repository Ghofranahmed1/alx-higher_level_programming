#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print("{}".format(my_list[i]))
            i += 1
        return(x)
    except IndexError:
        for item in my_list[i:]:
            print("{}".format(item))
        return (i)
