from skimage import data
from matplotlib import pyplot as plt

image = data.coffee()   #载入测试图像
radio = 128             #设置量化比率
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        for k in range(image.shape[2]):
            #对图像中的每一个像素进行量化
            image[i][j][k] = int(image[i][j][k]/radio)*radio
#打印量化后的图像
plt.imshow(image)
plt.show()
