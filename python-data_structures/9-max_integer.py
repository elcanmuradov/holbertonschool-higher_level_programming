#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    return my_list.sort().reverse()[0]