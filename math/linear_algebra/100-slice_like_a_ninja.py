#!/usr/bin/env python3

"""Module providing a function to slice a"""


def np_slice(matrix, axes={}):
    """
    Slice a NumPy-like array along specified axes.

    Args:
    matrix: Input array-like object to be sliced.
    axes (dict): Dictionary where keys are axes to slice along and
        values are tuples representing the slice for each axis.

    Returns:
    A new array resulting from the slicing.
    """
    # Create a list of slice objects for all dimensions
    slices = [slice(None)] * matrix.ndim

    # Update slices based on the provided axes
    for axis, slice_info in axes.items():
        slices[axis] = slice(*slice_info)

    # Apply the slices to the matrix
    return matrix[tuple(slices)].copy()
