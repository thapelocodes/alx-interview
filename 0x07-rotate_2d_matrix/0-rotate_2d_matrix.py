#!/usr/bin/python3
""" Rotates a `n` x `n` 2D matrix 90 degrees clockwise. """


def rotate_2d_matrix(matrix):
    """ Rotates a matrix in-place. """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()