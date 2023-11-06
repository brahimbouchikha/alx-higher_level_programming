#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    result = my_list.copy()
    my_list.clear()
    for i in range(len(result)):
        if i != idx:
            my_list.append(result[i])
    return my_list
