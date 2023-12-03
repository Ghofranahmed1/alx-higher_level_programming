#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = len(matrix)
    if not matrix:
        print()

    for i in range(x):
        y = len(matrix[i])
        for j in range(y):
            print("{:d}".format(matrix[i][j]), end=" ")
        print()
