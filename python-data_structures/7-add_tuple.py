#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > len(tuple_b):
        for k in range(0, len(tuple_a)):
            if tuple_b[k] == None:
                tuple_b[k] = 0
    else:
            for i in range(0, len(tuple_b)):
                if tuple_a[i] == None:
                    tuple_a[i] = 0
    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_c