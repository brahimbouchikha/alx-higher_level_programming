#!/usr/bin/python3
from sys import argv, maxsize
if __name__ == "__main__":
    _sum_ = 0
    for i in range(1, len(argv)):
        _sum_ += int(argv[i])
    if abs(_sum_) <= maxsize:
        print("{}".format(_sum_))
