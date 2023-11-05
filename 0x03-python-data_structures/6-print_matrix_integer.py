#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in matrix[i]:
            print('{:d} '.format(j), end='')
        print()
