import skimage.data as data
import matplotlib.pyplot as plt

image = data.coffee()  # 载入RGB图像
fig = plt.figure()
plt.axis('off')  # 不显示坐标轴
plt.imshow(image)  # 显示RGB彩色图像

# R 通道图像
imageR = image[:, :, 0]
plt.figure()
plt.axis('off')  # 不显示坐标轴
plt.imshow(imageR, cmap='gray')

# G 通道图像
imageG = image[:, :, 1]
plt.figure()
plt.axis('off')  # 不显示坐标轴
plt.imshow(imageG, cmap='gray')

# B 通道图像
imageB = image[:, :, 2]
plt.figure()
plt.axis('off')  # 不显示坐标轴
plt.imshow(imageB, cmap='gray')

plt.show()