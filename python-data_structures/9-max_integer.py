#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    temp = my_list[0]
    for i in range(1, len(my_list)):
        if temp < my_list[i]:
            temp = my_list
    return temp