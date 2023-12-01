#!/usr/bin/python3
"""Represents a square."""

class Square:
    """
    

    Attributes:
        __size (int): Size of a side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): Size of a side of the square (default is 0).
        Returns:
            None
        """
        self.size = size

    def area(self):
        """
        Calculates the square's area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter for __size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for __size.

        Args:
            value (int): Size of a side of the square.
        Returns:
            None
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """
        Prints the square.

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
