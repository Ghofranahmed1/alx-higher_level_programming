#!/usr/bin/python3
"""
 class MyList that inherits from list
 """
class Mylist(list):
    """ Public instance method that print a sorted list"""
    pass

    def print_sorted(self):
        print(sorted(list(self)))
