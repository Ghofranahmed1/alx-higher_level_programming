#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dic = dict(a_dictionary)
    for k, v in my_dic.items():
        my_dic[k] = v * 2
    return my_dic
