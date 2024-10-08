#!/usr/bin/env python3
"""
A function that calculates the adjugate
"""


def adjugate(matrix):
    """
    returns a matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0\
       or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is squares
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    def submatrix(mat, i, j):
        return [row[:j] + row[j+1:] for row in (mat[:i] + mat[i+1:])]

    def determinant(mat):
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for j in range(len(mat)):
            det += ((-1) ** j) * mat[0][j] * determinant(submatrix(mat, 0, j))
        return det

    if n == 1:
        return [[1]]

    cofactor_matrix = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            sign = (-1) ** (i + j)
            minor = determinant(submatrix(matrix, i, j))
            cofactor_row.append(sign * minor)
        cofactor_matrix.append(cofactor_row)

    # Transpose the cofactor matrix to get the adjugate matrix
    adjugate_matrix = [
        [cofactor_matrix[j][i] for j in range(n)]
        for i in range(n)
    ]

    return adjugate_matrix
