#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    for i in range(0,len(matrix)):
        for k in range(0,len(matrix[i])):
            new_matrix[i][k] = matrix[i][k] ** 2
    return new_matrix
