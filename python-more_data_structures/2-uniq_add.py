#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    uniq = []
    for i in my_list:
        if uniq.find(i) == -1:
            sum += i
            uniq.append(i)
    return sum
    