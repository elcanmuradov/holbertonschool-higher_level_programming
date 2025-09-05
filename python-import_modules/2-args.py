#!/usr/bin/python3

if __name__ == "__main__":
    count = len(argv)
    if count > 1:
        print("{a} arguments:".format(count))
        for i in (1,count + 1):
            print("{a}: {argv}".format(i,args[i]))
    elif count == 1:
        print("{a} argument:".format(count))
        print("{a}: {arg}".format(count,argv[1]))
    else:
        print("{a} arguments.".format(count))
