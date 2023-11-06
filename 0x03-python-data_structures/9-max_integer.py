#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 'None'
    _max_ = my_list[0]
    for i in range(1, len(my_list)):
        if _max_ < my_list[i]:
            _max_ = my_list[i]
    return _max_
