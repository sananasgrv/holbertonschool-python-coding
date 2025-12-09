#!/usr/bin/python3
"""Commment"""


class Square:
    """Square class"""
    def area(self):
        self.area = self.__size**2
        return self.area

    def size(self):
        return self.__size
    def size(self, value):
        if not self.__size is int:
            raise TypeError("size must be an integer")
        elif self.__size < 0 :
            raise ValueError("size must be >= 0")
def main():

main()