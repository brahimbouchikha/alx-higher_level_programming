#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    if chr(i) == 'q' or  chr(i) == 'e':
        continue
    print("{:c}".format(i), end='')
