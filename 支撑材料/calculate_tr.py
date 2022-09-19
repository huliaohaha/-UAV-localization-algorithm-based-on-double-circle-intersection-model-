from sympy import *


def calculate_cos(x1, x2, y1, y2):
    a = (x1 * x2 + y1 * y2) / (sqrt(x1 ** 2 + y1 ** 2) * sqrt(x2 ** 2 + y2 ** 2))
    return a


def calculate_sin(x1, x2, y1, y2):
    a = sqrt(1 - calculate_cos(x1, x2, y1, y2) ** 2)
    return a


def calculate_tan(x1, x2, y1, y2):
    a = calculate_sin(x1, x2, y1, y2) / calculate_cos(x1, x2, y1, y2)
    return a
