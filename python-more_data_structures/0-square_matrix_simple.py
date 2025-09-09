#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for i in range(0,len(matrix)):
        for k in range(0,len(matrix[i])):
            matrix[i][k] = matrix[i][k] ** 2
    return matrix
