#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = len(matrix)
    for i in range(x):
        y = len(matrix[i])
        for j in range(y):
            print(matrix[i][j], end=" ")
        print()
