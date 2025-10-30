# sphere.py
import math

def area(radius):
    """Return surface area of sphere"""
    return 4 * math.pi * radius ** 2

def perimeter(radius):
    """Return circumference of great circle of sphere"""
    return 2 * math.pi * radius
