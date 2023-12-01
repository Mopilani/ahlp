#!/usr/bin/python3
"""
Defines a Square class

This module provides a simple Square class.
"""


class Square:
    """square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes the square
        Args:
            size (int): side of the square
        Returns: None
        """
        self.__size = size
