#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        Sum = 0
        prevalue = 0
        my_dirc = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        for i in reversed(roman_string):
            value = my_dirc[i]
            if value < prevalue:
                Sum -= value
            else:
                Sum += value
            prevalue = value
        return Sum
