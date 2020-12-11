#RGB图像灰度化代码
from skimage import data
from matplotlib import pyplot as plt
import numpy as np
image = data.coffee()

#初始化灰度图像
max_gray = np.zeros(image.shape[0:2],dtype='uint8')
ave_gray = np.zeros(image.shape[0:2],dtype='uint8')
weight_gray = np.zeros(image.shape[0:2],dtype='uint8')
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        r,g,b = image[i,j,:]
        #最大灰度化方法
        max_gray[i,j] = max(r,g,b)
        #平均值灰度化方法
        ave_gray[i,j] = (r + g + b)/3
        #加权平均灰度化方法
        weight_gray[i,j] = 0.30*r+0.59*g+0.11*b

#显示结果
#显示RGB图像
plt.figure()
plt.axis('off')
plt.imshow(image)
#显示最大值灰度化图像
plt.figure()
plt.axis('off')
plt.imshow(max_gray,cmap='gray')
#显示平均值灰度化图像
plt.figure()
plt.axis('off')
plt.imshow(ave_gray,cmap='gray')
#显示加权平均灰度化图像
plt.figure()
plt.axis('off')
plt.imshow(weight_gray,cmap='gray')
plt.show()