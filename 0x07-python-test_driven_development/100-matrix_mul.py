#!/usr/bin/python3
"""This module contain a function that multiplies two matrix"""


def matrix_mul(m_a, m_b):
    """matrix_mul function that multiplies two matrix
    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    # variables to verify if both m_a and m_b can be multiplied
    nc1 = 0
    nr2 = 0

    # Check requirements for matrix m_a
    if m_a == []:
        raise ValueError("m_a can't be empty")
    for row1 in m_a:
        if type(row1) != list:
            raise TypeError("m_a must be a list of lists")
        len1 = len(m_a[0])
        if row1 == []:
            raise ValueError("m_a can't be empty")
        if len1 != len(row1):
            raise TypeError("each row of m_a must be of the same size")
        nc1 = len(row1)
        for column1 in row1:
            if type(column1) != int and type(column1) != float:
                raise TypeError("m_a should contain only integers or floats")

    # Check requirements for matrix m_b
    if m_b == []:
        raise ValueError("m_b can't be empty")
    for row2 in m_b:
        if type(row2) != list:
            raise TypeError("m_b must be a list of lists")
        len2 = len(m_b[0])
        if row2 == []:
            raise ValueError("m_b can't be empty")
        if len2 != len(row2):
            raise TypeError("each row of m_b must be of the same size")
        nr2 += 1
        for column2 in row2:
            if type(column2) != int and type(column2) != float:
                raise TypeError("m_b should contain only integers or floats")

    # Check if the multiplication is posible
    if nc1 != nr2:
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_prod = []

    for row_1 in m_a:
        l = 0
        l_row = []
        while l < len(m_b[0]):
            res = 0
            k = 0
            for column_1 in row_1:
                res += column_1 * m_b[k][l]
                k += 1
            l_row.append(res)
            l += 1
        matrix_prod.append(l_row)

    return matrix_prod
