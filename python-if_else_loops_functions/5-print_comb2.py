#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        str = "0" + str(i)
        print(str, sep=", ",end=", ")
    else: 
        print(i , sep=", ")
