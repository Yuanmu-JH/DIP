# 使用求均值的方法进行图像模拟采样
# 导入所需要的包
from skimage import data
from matplotlib import pyplot as plt #绘图包
import numpy as np
# 载入测试图像
image = data.coffee()
#显示原始图像的大小
print(image.shape)
# 显示图像类型
print(type(image))
# 设置采样比率
ratio=20
# 设置采样后的图像大小
image1 = np.zeros((int(image.shape[0]/ratio),int(image.shape[1]/ratio),image.shape[2]),dtype="int32")
# 通过循环对图像进行遍历
for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        for k in range(image1.shape[2]):
            # 获取需要采样的图像块
            delta=image[i*ratio:(i+1)*ratio,j*ratio:(j+1)*ratio,k]
            # 计算均值并存入图像结果
            image1[i,j,k] = np.mean(delta)    #均值采样
            # image1[i,j,k] = np.max(delta)      #最大值采样
# 打印采样后的图像
plt.imshow(image1)
plt.show()