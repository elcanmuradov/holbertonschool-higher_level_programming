#!/usr/bin/python3

if __name__ == "__main__":
    argv = sys.argv
    count = len(argv) - 1
    s = 0
    for i in range(1, count + 1):
        s += argv[i]
    print(s)
