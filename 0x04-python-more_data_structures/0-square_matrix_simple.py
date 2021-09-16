#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        squares = list(map(list, matrix))
        for i in range(len(squares)):
            for j in range(len(squares)):
                squares[i][j]**=2
    return squares
