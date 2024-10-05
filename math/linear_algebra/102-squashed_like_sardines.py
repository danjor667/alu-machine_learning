#!/usr/bin/env python3

"""Module providing a function to concatenate"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenate two matrices along a specified axis.

    Args:
    mat1 (list): First input matrix (list of lists of ints or floats).
    mat2 (list): Second input matrix (list of lists of ints or floats).
    axis (int): Axis along which to concatenate. Default is 0.

    Returns:
    list or None: A new matrix resulting from the concatenation,
        or None if concatenation is not possible.
    """
    # Check if inputs are lists
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    # Check if matrices are non-empty
    if not mat1 or not mat2:
        return None

    # Check if all rows are lists
    if not all(isinstance(row, list) for row in mat1 + mat2):
        return None

    if axis == 0:
        # Vertical concatenation
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        # Horizontal concatenation
        if len(mat1) != len(mat2):
            return None
        return [row1[:] + row2[:] for row1, row2 in zip(mat1, mat2)]
    else:
        # Invalid axis
        return None
