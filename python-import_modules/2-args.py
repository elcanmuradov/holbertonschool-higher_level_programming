#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv
    count = len(argv)
    if count > 1:
        print("{} arguments:".format(count))
        for i in (1,count + 1):
            print("{}: {}".format(i,argv[i]))
    elif count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(count,argv[1]))
    else:
        print("{} arguments.".format(count))
