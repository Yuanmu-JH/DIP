from skimage import data, color
from matplotlib import pyplot as plt
import numpy as np

L = 255


# 定义灰度值到彩色变换
def getR(gray):
    if gray < L / 2:
        return 0
    elif gray > L / 4 * 3:
        return L
    else:
        return 4 * gray - 2 * L


def getG(gray):
    if gray < L / 4:
        return 4 * gray
    elif gray > L / 4 * 3:
        return 4 * L - 4 * gray
    return L


def getB(gray):
    if gray < L / 4:
        return L
    elif gray > L / 2:
        return 0
    else:
        return 2 * L - 4 * gray


# 设置字体格式
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 15
plt.rcParams['axes.unicode_minus'] = False
x = [0, 64, 127, 191, 255]

# 绘制灰度图像到R通道的映射关系
plt.figure()
R = []
for i in x:
    R.append(getR(i))
plt.plot(x, R, 'r', label='红色变换')
plt.legend(loc='best')

# 绘制灰度图像到R通道的映射关系
plt.figure()
G = []
for i in x:
    G.append(getG(i))
plt.plot(x, G, 'g', label='绿色变换')
plt.legend(loc='best')

# 绘制灰度图像到B通道的映射关系
plt.figure()
B = []
for i in x:
    B.append(getB(i))
plt.plot(x, B, 'b', marker='o', markersize='5', label='绿色变换')
plt.legend(loc='best')

# 绘制灰度图像到RGB的映射关系
plt.figure()
plt.plot(x, R, 'r')
plt.plot(x, G, 'g')
plt.plot(x, B, 'b', marker='o', markersize='5')

plt.show()
