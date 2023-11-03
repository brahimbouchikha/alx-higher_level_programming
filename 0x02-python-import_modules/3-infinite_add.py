#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    _sum_ = 0
    for i in range(1, len(argv)):
        _sum_ += int(argv[i])
    print("{:d}".format(_sum_))

