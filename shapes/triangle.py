#!/usr/bin/env python

"""
Author: Russ
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains a length value
    and width value.
    """

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def area(self):
        """
        Compute the area using the formula 1/2 * length * width
        """
        return 1/2 * (self.height * self.width)

    def perimeter(self):
        """
        Compute the perimeter using the formula length + width + height
        """
        return self.length + self.width + self.height


