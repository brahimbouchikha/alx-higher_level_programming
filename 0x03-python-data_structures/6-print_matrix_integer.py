#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = ' '.join(str(i) for i in row)
        print(line)
