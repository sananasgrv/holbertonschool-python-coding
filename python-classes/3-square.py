#!/usr/bin/python3
"""Commment"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        self.size = size
    def size(self):
        return self.__size
    def size(self, value):
        if not self.__size is int:
            raise TypeError("size must be an integer")
        elif self.__size < 0 :
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        self.area = self.size**2
        return self.area
