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
    Represents a Triangle shape, and contains side "a", side "b", and side "c" values
    """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """
        Compute the area using the Heron's formula: a=sqrt(s(s-a)(s-b)(s-c)
        """
        p = (self.a + self.b + self.c) / 2
        q = p*(p-self.a)*(p-self.b)*(p-self.c)
        sqrt(q)
        return round(q, 2)


    def perimeter(self):
        """
        Compute the perimeter using the formula: sum of sides,  p = a + b + c
        """
        return self.a + self.b + self.c
