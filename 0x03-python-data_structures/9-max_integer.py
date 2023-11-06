#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 'None'
    _max_ = 0
    for i in my_list:
        if _max_ < i:
            _max_ = i
    return _max_
