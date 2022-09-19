from Trans import *
from calculate_tr import *

r, j, a_oi, a_oj, a_ij = symbols('R, j, a1, a2, a3')
x = Symbol('x')
y = Symbol('y')

pos_i = (to_z_j(r, i * 40))
pos_j = (to_z_j(r, j * 40))
"""i的直角坐标"""
i_x1, i_x2 = pos_i
"""j的直角坐标"""
j_x1, j_x2 = pos_j

"""
第二个圆的计算程序
"""
[a, b] = (solve([sqrt(((x - r * cos(2 * pi * j / 9) / 2) ** 2) + (y - r * sin(2 * pi * j / 9) / 2) ** 2) - r / (
        2 * tan(a_oi)),
                 (x - r * cos(2 * pi * j / 9) / 2) * (r * cos(2 * pi * j / 9)) - (y - r * sin(2 * pi * j / 9) / 2) * (
                         r * sin(2 * pi * j / 9))], x, y))

"""把两组解分别保存在a和b中"""
(b_x1, b_y1) = a
(b_x2, b_y2) = b

b_x1_1 = (b_x1 - (r * cos(2 * pi * j) / 9)) / 2
b_y1_1 = (b_y1 - (r * sin(2 * pi * j) / 9)) / 2
b_x1_2 = r * cos(2 * pi * j) / 9
b_y1_2 = r * sin(2 * pi * r) / 9

b_x2_1 = (b_x2 - (r * cos(2 * pi * j) / 9)) / 2
b_y2_1 = (b_y2 - (r * sin(2 * pi * j) / 9)) / 2
b_x2_2 = r * cos(2 * pi * j) / 9
b_y2_2 = r * sin(2 * pi * r) / 9

"""分别计算两组解的正弦值，对于第二个圆，应舍去小于0的解"""
b_sin_1 = calculate_sin(b_x1_1, b_x1_2, b_y1_1, b_y1_2)
b_sin_2 = calculate_sin(b_x2_1, b_x2_2, b_y2_1, b_y2_2)
"""求第二个圆的半径"""
r_2 = r / (sin(a_oj))

