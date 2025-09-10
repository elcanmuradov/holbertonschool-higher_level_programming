#!/usr.bin/python3

def only_diff_elements(set_1, set_2):
    common_list = []
    new_list = []
    for i in set_1:
        for k in set_2:
            if i == k:
                common_list.append(i)
    sum_list = set_1 + set_2
    for a in sum_list:
        for b in common_list:
            if a != b:
                new_list.append(a)
