from skimage import data,color
from matplotlib import pyplot as plt
import numpy as np
img  = data.coffee()
grayimg = color.rgb2gray(img)   #将彩色图像转换为灰度图像
plt.figure()
plt.axis('off')
plt.imshow(grayimg,cmap='gray') #显示灰度图像
rows,cols = grayimg.shape
labels = np.zeros([[rows,cols]])
for i in range(rows):
    for j in range(cols):
        if(grayimg[i,j] < 0.4):
            labels[i,j] = 0
        elif(grayimg[i,j] < 0.8):
            labels[i,j] = 1
        else:
            labels[i,j] = 2
psdimg = color.rgb2gray(labels) #不同的灰度区间采用不同的颜色
plt.figure()
plt.axis('off')
plt.imshow(psdimg)  #显示强度分层图像