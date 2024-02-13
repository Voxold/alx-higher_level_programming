#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_matrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j * j)
        n_matrix.append(row)
    return (n_matrix)
