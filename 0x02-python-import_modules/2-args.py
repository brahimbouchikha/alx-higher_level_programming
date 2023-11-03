#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argv_count = len(argv)
    if argv_count == 2:
        print("1 argument:")
    elif argv_count == 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(argv_count - 1))
    for i in range(1, argv_count):
        print("{:d}: {:s}".format(i, argv[i]))
