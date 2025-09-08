#!/usr/bin/python3

def no_c(my_string):
    n = my_string.find("c")
    while True:
        if n == -1:
            break
        begin = my_string[:n]
        end = my_string[n + 1:]
        my_string = begin + end
        n = my_string.find("c")
    n = my_string.find("C")
    while True:
        if n == -1:
            break
        begin = my_string[:n]
        end = my_string[n + 1:]
        my_string = begin + end
        n = my_string.find("C")
    return my_string
