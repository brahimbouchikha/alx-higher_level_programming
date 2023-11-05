#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for i in row:
            count += 1
            print('{:d}'.format(i), end='')
            if count < len(row):
                print(' ', end='')

        print()
