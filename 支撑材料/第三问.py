from calculate_angle import *
import sympy as sym


def to_z_hd(l, theta):
    """
        极坐标转换为直角坐标
        输入的角度为角度制
        """
    x = l * cos(theta * pi / 180)
    y = l * sin(theta * pi / 180)
    return x, y


"""假设半径的值为100"""
r = float(100)

fy_h = [(0, 0), (r, 0), (r, 40), (r, 80), (r, 120), (r, 160), (r, 200), (r, 240), (r, 280), (r, 320)]

fy_j = []

for i in range(10):
    a, b = fy_h[i]
    fy_j.append(to_z_hd(a, b))

init_j_p = [(0, 0), (100, 0), (98, 40.1), (112, 80.21), (105, 119.75), (98, 159.86), (112, 199.96), (105, 240.07),
            (98, 280.17), (112, 320.28)]
init_z_p = []
x_p = []
y_p = []

for k in range(10):
    e, f = init_j_p[k]
    """init_z_p保存了初始状态下的"""
    init_z_p.append((to_z_hd(e, f)))
    g, h = init_z_p[k]
    x_p.append(g)
    y_p.append(h)

"""第二个飞行器"""

alpha021 = acos(((x_p[0] - x_p[2]) * (x_p[1] - x_p[2]) + (y_p[0] - y_p[2]) * (y_p[1] - y_p[2])) / (sqrt(
    (x_p[0] - x_p[2]) ** 2 + (y_p[0] - y_p[2]) ** 2) * sqrt(
    (x_p[1] - x_p[2]) ** 2 + (y_p[1] - y_p[2]) ** 2)))

alpha021 = alpha021 * 180 / pi

print(f"alpha021的初始角度为{alpha021}")

"""
参数
"""
count = 1
a = 0
"""计数器"""

while a <= 10:
    if alpha021 <= 70:
        while True:
            y_p[2] = y_p[2] - 0.1 * (10 ** (-a))
            alpha021 = acos(((x_p[0] - x_p[2]) * (x_p[1] - x_p[2]) + (y_p[0] - y_p[2]) * (y_p[1] - y_p[2])) / (sqrt(
                (x_p[0] - x_p[2]) ** 2 + (y_p[0] - y_p[2]) ** 2) * sqrt(
                (x_p[1] - x_p[2]) ** 2 + (y_p[1] - y_p[2]) ** 2)))
            alpha021 = alpha021 * 180 / pi
            print(f"第{count}次迭代,alpha021的值为{alpha021}")
            count += 1
            if alpha021 >= 70:
                a += 1
                break

    elif alpha021 >= 70:
        while True:
            y_p[2] = y_p[2] + 0.1 * (10 ** (-a))
            alpha021 = acos(((x_p[0] - x_p[2]) * (x_p[1] - x_p[2]) + (y_p[0] - y_p[2]) * (y_p[1] - y_p[2])) / (sqrt(
                (x_p[0] - x_p[2]) ** 2 + (y_p[0] - y_p[2]) ** 2) * sqrt(
                (x_p[1] - x_p[2]) ** 2 + (y_p[1] - y_p[2]) ** 2)))
            alpha021 = alpha021 * 180 / pi
            print(f"第{count}次迭代,alpha021的值为{alpha021}")
            count += 1
            if alpha021 <= 70:
                a += 1
                break

"""第九个飞行器"""
alpha091 = c_a(x_p[0] - x_p[9], y_p[0] - y_p[9], x_p[1] - x_p[9], (y_p[1] - y_p[9]))

alpha091 = alpha091 * 180 / pi

print(f"alpha091的初始角度为{alpha091}")

"""
参数
"""

"""计数器"""
count = 1

a = 0

while a <= 10:
    if alpha091 <= 70:
        while True:
            y_p[9] = y_p[9] + 0.1 * (10 ** (-a))
            alpha091 = c_a(x_p[0] - x_p[9], y_p[0] - y_p[9], x_p[1] - x_p[9], (y_p[1] - y_p[9]))
            alpha091 = alpha091 * 180 / pi
            print(f"第{count}次迭代,alpha091的值为{alpha091}")
            count += 1
            if alpha091 >= 70:
                a += 1
                break

    elif alpha091 >= 70:
        while True:
            y_p[9] = y_p[9] - 0.1 * (10 ** (-a))
            alpha091 = c_a(x_p[0] - x_p[9], y_p[0] - y_p[9], x_p[1] - x_p[9], (y_p[1] - y_p[9]))
            alpha091 = alpha091 * 180 / pi
            print(f"第{count}次迭代,alpha091的值为{alpha091}")
            count += 1
            if alpha091 <= 70:
                a += 1
                break

alpha029_true = 50
alpha092_true = 50
alpha029 = c_a(x_p[0] - x_p[2], y_p[0] - y_p[2], x_p[9] - x_p[2], (y_p[9] - y_p[2]))
alpha092 = c_a(x_p[0] - x_p[9], y_p[0] - y_p[9], x_p[2] - x_p[9], (y_p[2] - y_p[9]))
print(f"alpha029的值为{alpha029 * 180 / pi}")
print(f"alpha092的值为{alpha092 * 180 / pi}")


def c_a_sym(x1, y1, x2, y2):
    theta = sym.acos((x1 * x2 + y1 * y2) / (sym.sqrt(
        x1 ** 2 + y1 ** 2) * sym.sqrt(
        x2 ** 2 + y2 ** 2)))
    return theta


x = sym.Symbol('x')
y = sym.Symbol("y")
(x1, y1), (x2, y2) = (sym.solve([x - 50, c_a_sym(-x, -y, x_p[1] - x, y_p[1] - y) * 180 / pi - 2 * alpha021], x, y))

if y1 > 0:
    y_true = y1
    x_true = x1
else:
    y_true = y2
    x_true = x2

print(x_true, y_true)
