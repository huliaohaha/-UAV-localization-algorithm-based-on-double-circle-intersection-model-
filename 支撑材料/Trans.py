from sympy import *


def to_z_j(l, theta):
    """
    极坐标转换为直角坐标
    输入的角度为角度制
    """
    x = l * cos(theta * pi / 180)
    y = l * sin(theta * pi / 180)
    return x, y


def to_z_h(l, theta):
    """
    极坐标转换为直角坐标
    输入的角度为弧度制
    """
    x = l * cos(theta)
    y = l * sin(theta)
    return x, y


def to_j(x, y):
    """直角坐标转换为极坐标"""
    if x > 0 and y > 0:
        l1 = sqrt(x ** 2 + y ** 2)
        t1 = (atan(y / x)) * 180 / pi
        return l1, t1
    if x < 0 and y > 0:
        l2 = sqrt(x ** 2 + y ** 2)
        t2 = (atan(y / abs(x))) * 180 / pi + 90
        return l2, t2
    if x < 0 and y < 0:
        l3 = sqrt(x ** 2 + y ** 2)
        t3 = (atan(abs(y) / abs(x))) * 180 / pi + 180
        return l3, t3
    if x > 0 and y < 0:
        l4 = sqrt(x ** 2 + y ** 2)
        t4 = (atan(abs(y) / x)) * 180 / pi + 270
        return l4, t4
