from math import *


def c_a(x1, y1, x2, y2):
    theta = acos((x1 * x2 + y1 * y2) / (sqrt(
        x1 ** 2 + y1 ** 2) * sqrt(
        x2 ** 2 + y2 ** 2)))
    return theta
