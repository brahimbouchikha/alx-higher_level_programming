#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    for i in range(2):
        result += ((tuple_a[i] + tuple_b[i]), )
    return result
