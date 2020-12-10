#灰度图像按以上映射关系转换为彩色图像
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


img = data.coffee()
gray_img = color.rgb2gray(img) * 255
color_img = np.zeros(img.shape, dtype='uint8')
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r, g, b = getR(gray_img[i, j]), getG(gray_img[i, j]), getB(gray_img[i, j])
        color_img[i, j, :] = (r, g, b)

plt.figure()
plt.axis('off')
plt.imshow(gray_img)

plt.figure()
plt.axis('off')
plt.imshow(color_img)

plt.show()