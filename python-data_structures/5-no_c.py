#!/usr/bin/python3

def no_c(my_string):
    my_string = my_string.list()
    for i in range(0, len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            del my_string[i]
    my_string = "".join(my_string)
    return my_string
