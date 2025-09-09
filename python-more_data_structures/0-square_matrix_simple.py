#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(0,len(new_matrix)):
        for k in range(0,len(new_matrix[i])):
            new_matrix[i][k] = matrix[i][k] ** 2
    return new_matrix
