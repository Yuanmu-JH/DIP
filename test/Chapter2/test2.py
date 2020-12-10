from skimage import data, io
from matplotlib import pyplot as plt
import math
import numpy as np
import sys

#定义RGB图像转换为HSI图像的函数
def RGB_to_HSI(r, g, b):
    r = r / 255
    g = g / 255
    b = b / 255
    num = 0.5 * ((r - g) + (r - b))
    den = ((r - g) * (r - g) + (r - b) * (g - b)) ** 0.5
    if b <= g:
        if den == 0:
            den = sys.float_info.min
        h = math.acos(num / den)
    elif b > g:
        if den == 0:
            den = sys.float_info.min
        h = (2 * math.pi) - math.acos(num / den)
    s = 1 - (3 * min(r, g, b) / (r + g + b))
    i = (r + g + b) / 3
    return int(h), int(s * 100), int(i * 255)


# image = io.imread('test.jpg')
image = data.coffee()
hsi_image = np.zeros(image.shape, dtype='uint8')
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        r, g, b = image[i, j, :]
        h, s, i = RGB_to_HSI(r, g, b)
        hsi_image[i, j, :] = (h, s, i)
        print(hsi_image[i, j, :])

plt.figure()
plt.axis('off')
plt.imshow(image)  # 显示RGB原图像

plt.figure()
plt.axis('off')
plt.imshow(image[:, :, 0], cmap='gray')  # 显示RGB原图像R分量

plt.figure()
plt.axis('off')
plt.imshow(image[:, :, 1], cmap='gray')  # 显示RGB原图像G分量

plt.figure()
plt.axis('off')
plt.imshow(image[:, :, 2], cmap='gray')  # 显示RGB原图像B分量

plt.figure()
plt.axis('off')
plt.imshow(hsi_image)  # 显示HSI图像

plt.figure()
plt.axis('off')
plt.imshow(hsi_image[:, :, 0], cmap='gray')  # 显示HSI图像H分量

plt.figure()
plt.axis('off')
plt.imshow(hsi_image[:, :, 1], cmap='gray')  # 显示HSI图像S分量

plt.figure()
plt.axis('off')
plt.imshow(hsi_image[:, :, 2], cmap='gray')  # 显示HSI图像I分量

plt.show()
