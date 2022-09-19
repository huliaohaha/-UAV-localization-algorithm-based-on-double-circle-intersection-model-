import matplotlib.pyplot as plt
import math

# 点数
N = 10

# 定义 散点半径
# r = 2 * np.random.rand(N)

r = [98.4, 112, 105, 98, 112, 105, 98, 112, 100, 0]

# 定义散点角度， math.radians用于将角度制转换为弧度制
# theta = 2 * np.pi * np.random.rand(N)
theta = [math.radians(40.1), math.radians(80.21), math.radians(119.75), math.radians(159.86), math.radians(199.96), math.radians(240.07),
         math.radians(280.17), math.radians(320.28), math.radians(360), math.radians(0)]
# 定义 面积
# area = 200 * r**2

# 定义散点颜色
colors = 'b'

# 绘制极坐标，111表示 1*1矩阵第1个
ax = plt.subplot(111, projection='polar')

# 绘制散点图，参数（角度、半径、颜色）
c = ax.scatter(theta, r, c=colors, cmap='hsv', alpha=1, )

# 图形绘制
plt.show()
