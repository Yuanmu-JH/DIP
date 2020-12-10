from skimage import data, color, io
from matplotlib import pyplot as plt
import numpy as np
import math

image = io.imread('test.png')
r = image[:, :, 0]
g = image[:, :, 1]
b = image[:, :, 2]
# RGB颜色空间中的分割
# 选择样本区域
r_template = r[128:255, 85:169]
# 计算该区域的彩色点的平均向量a的红色分量
r_template_u = np.mean(r_template)
# 计算样本点红色分量的标准差
r_template_d = 0.0
for i in range(r_template.shape[0]):
    for j in range(r_template.shape[1]):
        r_template_d = r_template_d + (r_template[i, j] - r_template_u) * (r_template[i, j] - r_template_u)

r_template_d = math.sqrt(r_template_d / r_template.shape[0] / r_template.shape[1])
# 寻找符合条件的点，r_cut为红色分割图像
r_cut = np.zeros(r.shape, dtype='uint8')
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        if r[i, j] >= (r_template_u - 1.25 * r_template_d) and r[i, j] <= (r_template_u + 1.25 * r_template_d):
            r_cut[i, j] = 1
# image_cut为根据红色分割后的RGB图像
image_cut = np.zeros(image.shape, dtype='uint8')
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        if r_cut[i, j] == 1:
            image_cut[i, j, :] = image[i, j, :]

plt.figure()
plt.axis('off')
plt.imshow(image)  # 显示原始图像

plt.figure()
plt.axis('off')
plt.imshow(r)  # 显示R图像

plt.figure()
plt.axis('off')
plt.imshow(g)  # 显示G图像

plt.figure()
plt.axis('off')
plt.imshow(b)  # 显示B图像

plt.figure()
plt.axis('off')
plt.imshow(r_cut)  # 显示红色分割图像图像

plt.figure()
plt.axis('off')
plt.imshow(image_cut)  # 显示分割后的RGB图像

plt.show()