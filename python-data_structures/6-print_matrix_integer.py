#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 0:
        for i in range(0, len(matrix)):
            for k in range(0, len(matrix[i])):
                if k != len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][k]), end=" ")
                else:
                    print("{:d}".format(matrix[i][k]))
    else:
        print()