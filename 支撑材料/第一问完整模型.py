from calculate_tr import *
import math

i = float(input("请输入第一架已知信号的飞机："))
j = float(input("请输入第二架已知信号的飞机："))
k = float(input("请输入未知信号的飞机："))
"""
输入的角度为角度制
"""
a_ij = float(input("请输入第夹角a_ij：")) * math.pi / 180
a_oj = float(input("请输入第夹角a_oj：")) * math.pi / 180
a_oi = float(input("请输入第夹角a_oi：")) * math.pi / 180
r = float(input("请输入半径大小："))

if k > j > i:
    if a_ij > a_oi and a_ij > a_oi:
        x = Symbol('x')
        y = Symbol('y')
        m = Symbol('m')
        n = Symbol('n')

        """
        第一个圆的计算程序
        """
        [a, b] = (
            solve([((x - r * cos(2 * math.pi * (i - 1) / 9) / 2) ** 2) + (
                    y - r * sin(2 * math.pi * (i - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oi))) ** 2,
                   (x - r * cos(2 * math.pi * (i - 1) / 9) / 2) * (r * cos(2 * math.pi * (i - 1) / 9)) + (
                           y - r * sin(2 * math.pi * (i - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (i - 1) / 9))], x, y))

        """把两组解分别保存在a和b中"""
        (a_x1, a_y1) = a
        (a_x2, a_y2) = b

        a_x1_1 = (a_x1 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y1_1 = (a_y1 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x1_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y1_2 = r * sin(2 * math.pi * (i - 1) / 9)

        a_x2_1 = (a_x2 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y2_1 = (a_y2 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x2_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y2_2 = r * sin(2 * math.pi * (i - 1) / 9)

        """分别计算两组解的正弦值，对于第一个圆，应舍去大于0的解"""
        a_sin_1 = -(a_x1_1 * a_y1_2 - a_x1_2 * a_y1_1)
        a_sin_2 = -(a_x2_1 * a_y2_2 - a_x2_2 * a_y2_1)
        print(a_sin_1)
        print(a_sin_2)
        if a_sin_1 > a_sin_2:
            a_x_true, a_y_true = b
        else:
            a_x_true, a_y_true = a

        print(f"第一个圆的圆心坐标为{a_x_true, a_y_true}")

        """求第一个圆的半径"""
        r_1 = r / (2 * (sin(a_oi)))
        print(f"第一个圆的半径是{r_1}")

        """
        第二个圆的计算程序
        """
        [e, f] = (
            solve([((m - r * cos(2 * math.pi * (j - 1) / 9) / 2) ** 2) + (
                    n - r * sin(2 * math.pi * (j - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oj))) ** 2,
                   (m - r * cos(2 * math.pi * (j - 1) / 9) / 2) * (r * cos(2 * math.pi * (j - 1) / 9)) + (
                           n - r * sin(2 * math.pi * (j - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (j - 1) / 9))], m, n))

        """把两组解分别保存在a和b中"""
        (b_x1, b_y1) = e
        (b_x2, b_y2) = f

        b_x1_1 = (b_x1 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y1_1 = (b_y1 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x1_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y1_2 = r * sin(2 * math.pi * (j - 1) / 2)

        b_x2_1 = (b_x2 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y2_1 = (b_y2 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x2_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y2_2 = r * sin(2 * math.pi * (j - 1) / 9)

        """分别计算两组解的正弦值，对于第二个圆，应舍去小于0的解"""
        b_sin_1 = -(b_x1_1 * b_y1_2 - b_x1_2 * b_y1_1)
        b_sin_2 = -(b_x2_1 * b_y2_2 - b_x2_2 * b_y2_1)
        if b_sin_1 > b_sin_2:
            b_x_true, b_y_true = e
        else:
            b_x_true, b_y_true = f

        print(f"第二个圆的圆心坐标为{b_x_true, b_y_true}")

        """求第二个圆的半径"""
        r_2 = r / (2 * (sin(a_oj)))
        print(f"第二个圆的半径是{r_2}")

        print((
            solve([(x - a_x1) ** 2 + (y - a_y1) ** 2 - r_1 ** 2, (x - b_x1) ** 2 + (y - b_y1) ** 2 - r_2 ** 2],
                  x,
                  y)))

    elif a_oi > a_ij and a_oi > a_oj:
        x = Symbol('x')
        y = Symbol('y')
        m = Symbol('m')
        n = Symbol('n')

        """
        第一个圆的计算程序
        """
        [a, b] = (
            solve([((x - r * cos(2 * math.pi * (i - 1) / 9) / 2) ** 2) + (
                    y - r * sin(2 * math.pi * (i - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oi))) ** 2,
                   (x - r * cos(2 * math.pi * (i - 1) / 9) / 2) * (r * cos(2 * math.pi * (i - 1) / 9)) + (
                           y - r * sin(2 * math.pi * (i - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (i - 1) / 9))], x, y))

        """把两组解分别保存在a和b中"""
        (a_x1, a_y1) = a
        (a_x2, a_y2) = b

        a_x1_1 = (a_x1 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y1_1 = (a_y1 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x1_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y1_2 = r * sin(2 * math.pi * (i - 1) / 9)

        a_x2_1 = (a_x2 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y2_1 = (a_y2 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x2_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y2_2 = r * sin(2 * math.pi * (i - 1) / 9)

        """分别计算两组解的正弦值，对于第一个圆，应舍去大于0的解"""
        a_sin_1 = -(a_x1_1 * a_y1_2 - a_x1_2 * a_y1_1)
        a_sin_2 = -(a_x2_1 * a_y2_2 - a_x2_2 * a_y2_1)
        print(a_sin_1)
        print(a_sin_2)
        if a_sin_1 > a_sin_2:
            a_x_true, a_y_true = b
        else:
            a_x_true, a_y_true = a

        print(f"第一个圆的圆心坐标为{a_x_true, a_y_true}")

        """求第一个圆的半径"""
        r_1 = r / (2 * (sin(a_oi)))
        print(f"第一个圆的半径是{r_1}")

        """
        第二个圆的计算程序
        """
        [e, f] = (
            solve([((m - r * cos(2 * math.pi * (j - 1) / 9) / 2) ** 2) + (
                    n - r * sin(2 * math.pi * (j - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oj))) ** 2,
                   (m - r * cos(2 * math.pi * (j - 1) / 9) / 2) * (r * cos(2 * math.pi * (j - 1) / 9)) + (
                           n - r * sin(2 * math.pi * (j - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (j - 1) / 9))], m, n))

        """把两组解分别保存在a和b中"""
        (b_x1, b_y1) = e
        (b_x2, b_y2) = f

        b_x1_1 = (b_x1 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y1_1 = (b_y1 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x1_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y1_2 = r * sin(2 * math.pi * (j - 1) / 2)

        b_x2_1 = (b_x2 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y2_1 = (b_y2 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x2_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y2_2 = r * sin(2 * math.pi * (j - 1) / 9)

        """分别计算两组解的正弦值，对于第二个圆，应舍去小于0的解"""
        b_sin_1 = -(b_x1_1 * b_y1_2 - b_x1_2 * b_y1_1)
        b_sin_2 = -(b_x2_1 * b_y2_2 - b_x2_2 * b_y2_1)
        if b_sin_1 > b_sin_2:
            b_x_true, b_y_true = f
        else:
            b_x_true, b_y_true = e

        print(f"第二个圆的圆心坐标为{b_x_true, b_y_true}")

        """求第二个圆的半径"""
        r_2 = r / (2 * (sin(a_oj)))
        print(f"第二个圆的半径是{r_2}")

        print((
            solve([(x - a_x1) ** 2 + (y - a_y1) ** 2 - r_1 ** 2, (x - b_x1) ** 2 + (y - b_y1) ** 2 - r_2 ** 2],
                  x,
                  y)))
    elif a_oj > a_ij and a_oj > a_oi:
        x = Symbol('x')
        y = Symbol('y')
        m = Symbol('m')
        n = Symbol('n')

        """
        第一个圆的计算程序
        """
        [a, b] = (
            solve([((x - r * cos(2 * math.pi * (i - 1) / 9) / 2) ** 2) + (
                    y - r * sin(2 * math.pi * (i - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oi))) ** 2,
                   (x - r * cos(2 * math.pi * (i - 1) / 9) / 2) * (r * cos(2 * math.pi * (i - 1) / 9)) + (
                           y - r * sin(2 * math.pi * (i - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (i - 1) / 9))], x, y))

        """把两组解分别保存在a和b中"""
        (a_x1, a_y1) = a
        (a_x2, a_y2) = b

        a_x1_1 = (a_x1 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y1_1 = (a_y1 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x1_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y1_2 = r * sin(2 * math.pi * (i - 1) / 9)

        a_x2_1 = (a_x2 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y2_1 = (a_y2 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x2_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y2_2 = r * sin(2 * math.pi * (i - 1) / 9)

        """分别计算两组解的正弦值，对于第一个圆，应舍去大于0的解"""
        a_sin_1 = -(a_x1_1 * a_y1_2 - a_x1_2 * a_y1_1)
        a_sin_2 = -(a_x2_1 * a_y2_2 - a_x2_2 * a_y2_1)
        print(a_sin_1)
        print(a_sin_2)
        if a_sin_1 > a_sin_2:
            a_x_true, a_y_true = a
        else:
            a_x_true, a_y_true = b

        print(f"第一个圆的圆心坐标为{a_x_true, a_y_true}")

        """求第一个圆的半径"""
        r_1 = r / (2 * (sin(a_oi)))
        print(f"第一个圆的半径是{r_1}")

        """
        第二个圆的计算程序
        """
        [e, f] = (
            solve([((m - r * cos(2 * math.pi * (j - 1) / 9) / 2) ** 2) + (
                    n - r * sin(2 * math.pi * (j - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oj))) ** 2,
                   (m - r * cos(2 * math.pi * (j - 1) / 9) / 2) * (r * cos(2 * math.pi * (j - 1) / 9)) + (
                           n - r * sin(2 * math.pi * (j - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (j - 1) / 9))], m, n))

        """把两组解分别保存在a和b中"""
        (b_x1, b_y1) = e
        (b_x2, b_y2) = f

        b_x1_1 = (b_x1 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y1_1 = (b_y1 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x1_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y1_2 = r * sin(2 * math.pi * (j - 1) / 2)

        b_x2_1 = (b_x2 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y2_1 = (b_y2 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x2_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y2_2 = r * sin(2 * math.pi * (j - 1) / 9)

        """分别计算两组解的正弦值，对于第二个圆，应舍去小于0的解"""
        b_sin_1 = -(b_x1_1 * b_y1_2 - b_x1_2 * b_y1_1)
        b_sin_2 = -(b_x2_1 * b_y2_2 - b_x2_2 * b_y2_1)
        if b_sin_1 > b_sin_2:
            b_x_true, b_y_true = e
        else:
            b_x_true, b_y_true = f

        print(f"第二个圆的圆心坐标为{b_x_true, b_y_true}")

        """求第二个圆的半径"""
        r_2 = r / (2 * (sin(a_oj)))
        print(f"第二个圆的半径是{r_2}")

        print((
            solve([(x - a_x1) ** 2 + (y - a_y1) ** 2 - r_1 ** 2, (x - b_x1) ** 2 + (y - b_y1) ** 2 - r_2 ** 2],
                  x,
                  y)))


elif j > k > i:
    if a_ij > a_oi and a_ij > a_oi:
        x = Symbol('x')
        y = Symbol('y')
        m = Symbol('m')
        n = Symbol('n')

        """
        第一个圆的计算程序
        """
        [a, b] = (
            solve([((x - r * cos(2 * math.pi * (i - 1) / 9) / 2) ** 2) + (
                    y - r * sin(2 * math.pi * (i - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oi))) ** 2,
                   (x - r * cos(2 * math.pi * (i - 1) / 9) / 2) * (r * cos(2 * math.pi * (i - 1) / 9)) + (
                           y - r * sin(2 * math.pi * (i - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (i - 1) / 9))], x, y))

        """把两组解分别保存在a和b中"""
        (a_x1, a_y1) = a
        (a_x2, a_y2) = b

        a_x1_1 = (a_x1 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y1_1 = (a_y1 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x1_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y1_2 = r * sin(2 * math.pi * (i - 1) / 9)

        a_x2_1 = (a_x2 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y2_1 = (a_y2 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x2_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y2_2 = r * sin(2 * math.pi * (i - 1) / 9)

        """分别计算两组解的正弦值，对于第一个圆，应舍去大于0的解"""
        a_sin_1 = -(a_x1_1 * a_y1_2 - a_x1_2 * a_y1_1)
        a_sin_2 = -(a_x2_1 * a_y2_2 - a_x2_2 * a_y2_1)
        print(a_sin_1)
        print(a_sin_2)
        if a_sin_1 > a_sin_2:
            a_x_true, a_y_true = a
        else:
            a_x_true, a_y_true = b

        print(f"第一个圆的圆心坐标为{a_x_true, a_y_true}")

        """求第一个圆的半径"""
        r_1 = r / (2 * (sin(a_oi)))
        print(f"第一个圆的半径是{r_1}")

        """
        第二个圆的计算程序
        """
        [e, f] = (
            solve([((m - r * cos(2 * math.pi * (j - 1) / 9) / 2) ** 2) + (
                    n - r * sin(2 * math.pi * (j - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oj))) ** 2,
                   (m - r * cos(2 * math.pi * (j - 1) / 9) / 2) * (r * cos(2 * math.pi * (j - 1) / 9)) + (
                           n - r * sin(2 * math.pi * (j - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (j - 1) / 9))], m, n))

        """把两组解分别保存在a和b中"""
        (b_x1, b_y1) = e
        (b_x2, b_y2) = f

        b_x1_1 = (b_x1 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y1_1 = (b_y1 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x1_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y1_2 = r * sin(2 * math.pi * (j - 1) / 2)

        b_x2_1 = (b_x2 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y2_1 = (b_y2 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x2_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y2_2 = r * sin(2 * math.pi * (j - 1) / 9)

        """分别计算两组解的正弦值，对于第二个圆，应舍去小于0的解"""
        b_sin_1 = -(b_x1_1 * b_y1_2 - b_x1_2 * b_y1_1)
        b_sin_2 = -(b_x2_1 * b_y2_2 - b_x2_2 * b_y2_1)
        if b_sin_1 > b_sin_2:
            b_x_true, b_y_true = f
        else:
            b_x_true, b_y_true = e

        print(f"第二个圆的圆心坐标为{b_x_true, b_y_true}")

        """求第二个圆的半径"""
        r_2 = r / (2 * (sin(a_oj)))
        print(f"第二个圆的半径是{r_2}")

        print((
            solve([(x - a_x1) ** 2 + (y - a_y1) ** 2 - r_1 ** 2, (x - b_x1) ** 2 + (y - b_y1) ** 2 - r_2 ** 2],
                  x,
                  y)))
    elif a_oi > a_ij and a_oi > a_oj:
        x = Symbol('x')
        y = Symbol('y')
        m = Symbol('m')
        n = Symbol('n')

        """
        第一个圆的计算程序
        """
        [a, b] = (
            solve([((x - r * cos(2 * math.pi * (i - 1) / 9) / 2) ** 2) + (
                    y - r * sin(2 * math.pi * (i - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oi))) ** 2,
                   (x - r * cos(2 * math.pi * (i - 1) / 9) / 2) * (r * cos(2 * math.pi * (i - 1) / 9)) + (
                           y - r * sin(2 * math.pi * (i - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (i - 1) / 9))], x, y))

        """把两组解分别保存在a和b中"""
        (a_x1, a_y1) = a
        (a_x2, a_y2) = b

        a_x1_1 = (a_x1 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y1_1 = (a_y1 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x1_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y1_2 = r * sin(2 * math.pi * (i - 1) / 9)

        a_x2_1 = (a_x2 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y2_1 = (a_y2 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x2_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y2_2 = r * sin(2 * math.pi * (i - 1) / 9)

        """分别计算两组解的正弦值，对于第一个圆，应舍去大于0的解"""
        a_sin_1 = -(a_x1_1 * a_y1_2 - a_x1_2 * a_y1_1)
        a_sin_2 = -(a_x2_1 * a_y2_2 - a_x2_2 * a_y2_1)
        print(a_sin_1)
        print(a_sin_2)
        if a_sin_1 > a_sin_2:
            a_x_true, a_y_true = a
        else:
            a_x_true, a_y_true = b

        print(f"第一个圆的圆心坐标为{a_x_true, a_y_true}")

        """求第一个圆的半径"""
        r_1 = r / (2 * (sin(a_oi)))
        print(f"第一个圆的半径是{r_1}")

        """
        第二个圆的计算程序
        """
        [e, f] = (
            solve([((m - r * cos(2 * math.pi * (j - 1) / 9) / 2) ** 2) + (
                    n - r * sin(2 * math.pi * (j - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oj))) ** 2,
                   (m - r * cos(2 * math.pi * (j - 1) / 9) / 2) * (r * cos(2 * math.pi * (j - 1) / 9)) + (
                           n - r * sin(2 * math.pi * (j - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (j - 1) / 9))], m, n))

        """把两组解分别保存在a和b中"""
        (b_x1, b_y1) = e
        (b_x2, b_y2) = f

        b_x1_1 = (b_x1 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y1_1 = (b_y1 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x1_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y1_2 = r * sin(2 * math.pi * (j - 1) / 2)

        b_x2_1 = (b_x2 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y2_1 = (b_y2 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x2_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y2_2 = r * sin(2 * math.pi * (j - 1) / 9)

        """分别计算两组解的正弦值，对于第二个圆，应舍去小于0的解"""
        b_sin_1 = -(b_x1_1 * b_y1_2 - b_x1_2 * b_y1_1)
        b_sin_2 = -(b_x2_1 * b_y2_2 - b_x2_2 * b_y2_1)
        if b_sin_1 > b_sin_2:
            b_x_true, b_y_true = e
        else:
            b_x_true, b_y_true = f

        print(f"第二个圆的圆心坐标为{b_x_true, b_y_true}")

        """求第二个圆的半径"""
        r_2 = r / (2 * (sin(a_oj)))
        print(f"第二个圆的半径是{r_2}")

        print((
            solve([(x - a_x1) ** 2 + (y - a_y1) ** 2 - r_1 ** 2, (x - b_x1) ** 2 + (y - b_y1) ** 2 - r_2 ** 2],
                  x,
                  y)))
    elif a_oj > a_ij and a_oj > a_oi:
        x = Symbol('x')
        y = Symbol('y')
        m = Symbol('m')
        n = Symbol('n')

        """
        第一个圆的计算程序
        """
        [a, b] = (
            solve([((x - r * cos(2 * math.pi * (i - 1) / 9) / 2) ** 2) + (
                    y - r * sin(2 * math.pi * (i - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oi))) ** 2,
                   (x - r * cos(2 * math.pi * (i - 1) / 9) / 2) * (r * cos(2 * math.pi * (i - 1) / 9)) + (
                           y - r * sin(2 * math.pi * (i - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (i - 1) / 9))], x, y))

        """把两组解分别保存在a和b中"""
        (a_x1, a_y1) = a
        (a_x2, a_y2) = b

        a_x1_1 = (a_x1 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y1_1 = (a_y1 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x1_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y1_2 = r * sin(2 * math.pi * (i - 1) / 9)

        a_x2_1 = (a_x2 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y2_1 = (a_y2 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x2_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y2_2 = r * sin(2 * math.pi * (i - 1) / 9)

        """分别计算两组解的正弦值，对于第一个圆，应舍去大于0的解"""
        a_sin_1 = -(a_x1_1 * a_y1_2 - a_x1_2 * a_y1_1)
        a_sin_2 = -(a_x2_1 * a_y2_2 - a_x2_2 * a_y2_1)
        print(a_sin_1)
        print(a_sin_2)
        if a_sin_1 > a_sin_2:
            a_x_true, a_y_true = b
        else:
            a_x_true, a_y_true = a

        print(f"第一个圆的圆心坐标为{a_x_true, a_y_true}")

        """求第一个圆的半径"""
        r_1 = r / (2 * (sin(a_oi)))
        print(f"第一个圆的半径是{r_1}")

        """
        第二个圆的计算程序
        """
        [e, f] = (
            solve([((m - r * cos(2 * math.pi * (j - 1) / 9) / 2) ** 2) + (
                    n - r * sin(2 * math.pi * (j - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oj))) ** 2,
                   (m - r * cos(2 * math.pi * (j - 1) / 9) / 2) * (r * cos(2 * math.pi * (j - 1) / 9)) + (
                           n - r * sin(2 * math.pi * (j - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (j - 1) / 9))], m, n))

        """把两组解分别保存在a和b中"""
        (b_x1, b_y1) = e
        (b_x2, b_y2) = f

        b_x1_1 = (b_x1 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y1_1 = (b_y1 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x1_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y1_2 = r * sin(2 * math.pi * (j - 1) / 2)

        b_x2_1 = (b_x2 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y2_1 = (b_y2 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x2_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y2_2 = r * sin(2 * math.pi * (j - 1) / 9)

        """分别计算两组解的正弦值，对于第二个圆，应舍去小于0的解"""
        b_sin_1 = -(b_x1_1 * b_y1_2 - b_x1_2 * b_y1_1)
        b_sin_2 = -(b_x2_1 * b_y2_2 - b_x2_2 * b_y2_1)
        if b_sin_1 > b_sin_2:
            b_x_true, b_y_true = f
        else:
            b_x_true, b_y_true = e

        print(f"第二个圆的圆心坐标为{b_x_true, b_y_true}")

        """求第二个圆的半径"""
        r_2 = r / (2 * (sin(a_oj)))
        print(f"第二个圆的半径是{r_2}")

        print((
            solve([(x - a_x1) ** 2 + (y - a_y1) ** 2 - r_1 ** 2, (x - b_x1) ** 2 + (y - b_y1) ** 2 - r_2 ** 2],
                  x,
                  y)))

elif j > i > k:
    if a_ij > a_oi and a_ij > a_oi:
        x = Symbol('x')
        y = Symbol('y')
        m = Symbol('m')
        n = Symbol('n')

        """
        第一个圆的计算程序
        """
        [a, b] = (
            solve([((x - r * cos(2 * math.pi * (i - 1) / 9) / 2) ** 2) + (
                    y - r * sin(2 * math.pi * (i - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oi))) ** 2,
                   (x - r * cos(2 * math.pi * (i - 1) / 9) / 2) * (r * cos(2 * math.pi * (i - 1) / 9)) + (
                           y - r * sin(2 * math.pi * (i - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (i - 1) / 9))], x, y))

        """把两组解分别保存在a和b中"""
        (a_x1, a_y1) = a
        (a_x2, a_y2) = b

        a_x1_1 = (a_x1 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y1_1 = (a_y1 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x1_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y1_2 = r * sin(2 * math.pi * (i - 1) / 9)

        a_x2_1 = (a_x2 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y2_1 = (a_y2 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x2_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y2_2 = r * sin(2 * math.pi * (i - 1) / 9)

        """分别计算两组解的正弦值，对于第一个圆，应舍去大于0的解"""
        a_sin_1 = -(a_x1_1 * a_y1_2 - a_x1_2 * a_y1_1)
        a_sin_2 = -(a_x2_1 * a_y2_2 - a_x2_2 * a_y2_1)
        print(a_sin_1)
        print(a_sin_2)
        if a_sin_1 > a_sin_2:
            a_x_true, a_y_true = b
        else:
            a_x_true, a_y_true = a

        print(f"第一个圆的圆心坐标为{a_x_true, a_y_true}")

        """求第一个圆的半径"""
        r_1 = r / (2 * (sin(a_oi)))
        print(f"第一个圆的半径是{r_1}")

        """
        第二个圆的计算程序
        """
        [e, f] = (
            solve([((m - r * cos(2 * math.pi * (j - 1) / 9) / 2) ** 2) + (
                    n - r * sin(2 * math.pi * (j - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oj))) ** 2,
                   (m - r * cos(2 * math.pi * (j - 1) / 9) / 2) * (r * cos(2 * math.pi * (j - 1) / 9)) + (
                           n - r * sin(2 * math.pi * (j - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (j - 1) / 9))], m, n))

        """把两组解分别保存在a和b中"""
        (b_x1, b_y1) = e
        (b_x2, b_y2) = f

        b_x1_1 = (b_x1 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y1_1 = (b_y1 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x1_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y1_2 = r * sin(2 * math.pi * (j - 1) / 2)

        b_x2_1 = (b_x2 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y2_1 = (b_y2 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x2_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y2_2 = r * sin(2 * math.pi * (j - 1) / 9)

        """分别计算两组解的正弦值，对于第二个圆，应舍去小于0的解"""
        b_sin_1 = -(b_x1_1 * b_y1_2 - b_x1_2 * b_y1_1)
        b_sin_2 = -(b_x2_1 * b_y2_2 - b_x2_2 * b_y2_1)
        if b_sin_1 > b_sin_2:
            b_x_true, b_y_true = e
        else:
            b_x_true, b_y_true = f

        print(f"第二个圆的圆心坐标为{b_x_true, b_y_true}")

        """求第二个圆的半径"""
        r_2 = r / (2 * (sin(a_oj)))
        print(f"第二个圆的半径是{r_2}")

        print((
            solve([(x - a_x1) ** 2 + (y - a_y1) ** 2 - r_1 ** 2, (x - b_x1) ** 2 + (y - b_y1) ** 2 - r_2 ** 2],
                  x,
                  y)))
    elif a_oi > a_ij and a_oi > a_oj:
        x = Symbol('x')
        y = Symbol('y')
        m = Symbol('m')
        n = Symbol('n')

        """
        第一个圆的计算程序
        """
        [a, b] = (
            solve([((x - r * cos(2 * math.pi * (i - 1) / 9) / 2) ** 2) + (
                    y - r * sin(2 * math.pi * (i - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oi))) ** 2,
                   (x - r * cos(2 * math.pi * (i - 1) / 9) / 2) * (r * cos(2 * math.pi * (i - 1) / 9)) + (
                           y - r * sin(2 * math.pi * (i - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (i - 1) / 9))], x, y))

        """把两组解分别保存在a和b中"""
        (a_x1, a_y1) = a
        (a_x2, a_y2) = b

        a_x1_1 = (a_x1 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y1_1 = (a_y1 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x1_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y1_2 = r * sin(2 * math.pi * (i - 1) / 9)

        a_x2_1 = (a_x2 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y2_1 = (a_y2 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x2_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y2_2 = r * sin(2 * math.pi * (i - 1) / 9)

        """分别计算两组解的正弦值，对于第一个圆，应舍去大于0的解"""
        a_sin_1 = -(a_x1_1 * a_y1_2 - a_x1_2 * a_y1_1)
        a_sin_2 = -(a_x2_1 * a_y2_2 - a_x2_2 * a_y2_1)
        print(a_sin_1)
        print(a_sin_2)
        if a_sin_1 > a_sin_2:
            a_x_true, a_y_true = b
        else:
            a_x_true, a_y_true = a

        print(f"第一个圆的圆心坐标为{a_x_true, a_y_true}")

        """求第一个圆的半径"""
        r_1 = r / (2 * (sin(a_oi)))
        print(f"第一个圆的半径是{r_1}")

        """
        第二个圆的计算程序
        """
        [e, f] = (
            solve([((m - r * cos(2 * math.pi * (j - 1) / 9) / 2) ** 2) + (
                    n - r * sin(2 * math.pi * (j - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oj))) ** 2,
                   (m - r * cos(2 * math.pi * (j - 1) / 9) / 2) * (r * cos(2 * math.pi * (j - 1) / 9)) + (
                           n - r * sin(2 * math.pi * (j - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (j - 1) / 9))], m, n))

        """把两组解分别保存在a和b中"""
        (b_x1, b_y1) = e
        (b_x2, b_y2) = f

        b_x1_1 = (b_x1 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y1_1 = (b_y1 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x1_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y1_2 = r * sin(2 * math.pi * (j - 1) / 2)

        b_x2_1 = (b_x2 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y2_1 = (b_y2 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x2_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y2_2 = r * sin(2 * math.pi * (j - 1) / 9)

        """分别计算两组解的正弦值，对于第二个圆，应舍去小于0的解"""
        b_sin_1 = -(b_x1_1 * b_y1_2 - b_x1_2 * b_y1_1)
        b_sin_2 = -(b_x2_1 * b_y2_2 - b_x2_2 * b_y2_1)
        if b_sin_1 > b_sin_2:
            b_x_true, b_y_true = f
        else:
            b_x_true, b_y_true = e

        print(f"第二个圆的圆心坐标为{b_x_true, b_y_true}")

        """求第二个圆的半径"""
        r_2 = r / (2 * (sin(a_oj)))
        print(f"第二个圆的半径是{r_2}")

        print((
            solve([(x - a_x1) ** 2 + (y - a_y1) ** 2 - r_1 ** 2, (x - b_x1) ** 2 + (y - b_y1) ** 2 - r_2 ** 2],
                  x,
                  y)))
    elif a_oj > a_ij and a_oj > a_oi:
        x = Symbol('x')
        y = Symbol('y')
        m = Symbol('m')
        n = Symbol('n')

        """
        第一个圆的计算程序
        """
        [a, b] = (
            solve([((x - r * cos(2 * math.pi * (i - 1) / 9) / 2) ** 2) + (
                    y - r * sin(2 * math.pi * (i - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oi))) ** 2,
                   (x - r * cos(2 * math.pi * (i - 1) / 9) / 2) * (r * cos(2 * math.pi * (i - 1) / 9)) + (
                           y - r * sin(2 * math.pi * (i - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (i - 1) / 9))], x, y))

        """把两组解分别保存在a和b中"""
        (a_x1, a_y1) = a
        (a_x2, a_y2) = b

        a_x1_1 = (a_x1 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y1_1 = (a_y1 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x1_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y1_2 = r * sin(2 * math.pi * (i - 1) / 9)

        a_x2_1 = (a_x2 - (r * cos(2 * math.pi * (i - 1) / 9)) / 2)
        a_y2_1 = (a_y2 - (r * sin(2 * math.pi * (i - 1) / 9)) / 2)
        a_x2_2 = r * cos(2 * math.pi * (i - 1) / 9)
        a_y2_2 = r * sin(2 * math.pi * (i - 1) / 9)

        """分别计算两组解的正弦值，对于第一个圆，应舍去大于0的解"""
        a_sin_1 = -(a_x1_1 * a_y1_2 - a_x1_2 * a_y1_1)
        a_sin_2 = -(a_x2_1 * a_y2_2 - a_x2_2 * a_y2_1)
        print(a_sin_1)
        print(a_sin_2)
        if a_sin_1 > a_sin_2:
            a_x_true, a_y_true = a
        else:
            a_x_true, a_y_true = b

        print(f"第一个圆的圆心坐标为{a_x_true, a_y_true}")

        """求第一个圆的半径"""
        r_1 = r / (2 * (sin(a_oi)))
        print(f"第一个圆的半径是{r_1}")

        """
        第二个圆的计算程序
        """
        [e, f] = (
            solve([((m - r * cos(2 * math.pi * (j - 1) / 9) / 2) ** 2) + (
                    n - r * sin(2 * math.pi * (j - 1) / 9) / 2) ** 2 - (r / (
                     2 * tan(a_oj))) ** 2,
                   (m - r * cos(2 * math.pi * (j - 1) / 9) / 2) * (r * cos(2 * math.pi * (j - 1) / 9)) + (
                           n - r * sin(2 * math.pi * (j - 1) / 9) / 2) * (
                           r * sin(2 * math.pi * (j - 1) / 9))], m, n))

        """把两组解分别保存在a和b中"""
        (b_x1, b_y1) = e
        (b_x2, b_y2) = f

        b_x1_1 = (b_x1 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y1_1 = (b_y1 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x1_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y1_2 = r * sin(2 * math.pi * (j - 1) / 2)

        b_x2_1 = (b_x2 - (r * cos(2 * math.pi * (j - 1) / 9)) / 2)
        b_y2_1 = (b_y2 - (r * sin(2 * math.pi * (j - 1) / 9)) / 2)
        b_x2_2 = r * cos(2 * math.pi * (j - 1) / 9)
        b_y2_2 = r * sin(2 * math.pi * (j - 1) / 9)

        """分别计算两组解的正弦值，对于第二个圆，应舍去小于0的解"""
        b_sin_1 = -(b_x1_1 * b_y1_2 - b_x1_2 * b_y1_1)
        b_sin_2 = -(b_x2_1 * b_y2_2 - b_x2_2 * b_y2_1)
        if b_sin_1 > b_sin_2:
            b_x_true, b_y_true = e
        else:
            b_x_true, b_y_true = f

        print(f"第二个圆的圆心坐标为{b_x_true, b_y_true}")

        """求第二个圆的半径"""
        r_2 = r / (2 * (sin(a_oj)))
        print(f"第二个圆的半径是{r_2}")

        print((
            solve([(x - a_x1) ** 2 + (y - a_y1) ** 2 - r_1 ** 2, (x - b_x1) ** 2 + (y - b_y1) ** 2 - r_2 ** 2],
                  x,
                  y)))
