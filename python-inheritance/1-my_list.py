#!/usr/bin/python3
"""Module that defines an an object"""


class MyList(list):
    def __init__(self,newList=[]):
        newList = self.newList

"""Print the sorted list """
    def print_sorted(self):
        newList = newList.sort()
        print(newList)
