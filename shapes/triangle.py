#!/usr/bin/env python

"""
Author: Russ
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape
from math import sqrt

class Triangle(Shape):
    """
    Represents a Triangle shape, and contains a length value
    and width value.
    """
    decimal_places = 2

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """
        Compute the area using the formula 1/2 * length * width
        """
        p = (self.a + self.b + self.c) / 2
        q = p*(p-self.a)*(p-self.b)*(p-self.c)
        sqrt(q)
        return round(q, 2)


    def perimeter(self):
        """
        Compute the perimeter using the formula length + width + height
        """
        return self.a + self.b + self.c
