#!/usr/bin/python3
def no_c(my_string):
    new_string = [x for x in my_string if x != 'c' and x != 'C']
    new_string = "".join(new_string)
    return new_string
