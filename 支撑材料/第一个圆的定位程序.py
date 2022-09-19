from Trans import *
from calculate_tr import *
import math

r, i, j, a_oi, a_oj, a_ij = symbols('R, i, j, a1, a2, a3')
"""特殊情况1：a1=a_io, a2=a_jo, a3=a_ij"""
x = Symbol('x')
y = Symbol('y')

pos_i = (to_z_j(r, i * 40))
pos_j = (to_z_j(r, j * 40))
"""i的直角坐标"""
i_x1, i_x2 = pos_i
"""j的直角坐标"""
j_x1, j_x2 = pos_j

"""第一个圆的计算程序"""
[a, b] = (solve([sqrt(((x - r * cos(2 * pi * i / 9) / 2) ** 2) + (y - r * sin(2 * pi * i / 9) / 2) ** 2) - r / (
        2 * tan(a_oi)),
                 (x - r * cos(2 * pi * i / 9) / 2) * (r * cos(2 * pi * i / 9)) - (y - r * sin(2 * pi * i / 9) / 2) * (
                         r * sin(2 * pi * i / 9))], x, y))

"""把两组解分别保存在a和b中"""
(a_x1, a_y1) = a
(a_x2, a_y2) = b

a_x1_1 = (a_x1 - (r * cos(2 * pi * i) / 9)) / 2
a_y1_1 = (a_y1 - (r * sin(2 * pi * i) / 9)) / 2
a_x1_2 = r * cos(2 * pi * i) / 9
a_y1_2 = r * sin(2 * pi * r) / 9

a_x2_1 = (a_x2 - (r * cos(2 * pi * i) / 9)) / 2
a_y2_1 = (a_y2 - (r * sin(2 * pi * i) / 9)) / 2
a_x2_2 = r * cos(2 * pi * i) / 9
a_y2_2 = r * sin(2 * pi * r) / 9

""""分别计算两组解的正弦值，对于第一个圆，应舍去大于0的解"""
a_sin_1 = calculate_sin(a_x1_1, a_x1_2, a_y1_1, a_y1_2)
a_sin_2 = calculate_sin(a_x2_1, a_x2_2, a_y2_1, a_y2_2)
"""求第一个圆的半径"""
r_1 = r / (sin(a_oi))
