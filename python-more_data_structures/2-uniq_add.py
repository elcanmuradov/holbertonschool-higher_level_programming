#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    uniq = []
    for i in my_list:
        if not (i in uniq):
            sum += i
            uniq.append(i)
    return sum
