#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    uniq = 0
    for i in my_list:
        sum += i
        for k in my_list:
            if i == k:
                uniq += k
    return sum - uniq
