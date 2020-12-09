#对比度操作
from matplotlib import pyplot as plt
from skimage import data
import numpy as np

def change_alpha(im,a):
    im_changed =np.zeros(shape=im.shape,dtype='uint8')
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            for k in range(im.shape[2]):
                if im[i,j,k]*a > 255:
                    im_changed[i,j,k] = 255
                elif im[i,j,k]*a <0:
                    im_changed[i,j,k] = 0
                else:
                    im_changed[i,j,k] = im[i,j,k]*a
    return  im_changed
#在一个figure上显示多个图像
fig = plt.figure()
image=data.coffee()
image1 = change_alpha(image,1)
ax = fig.add_subplot(221)
ax.imshow(image1)
image2 = change_alpha(image,0.2)
ax = fig.add_subplot(222)
ax.imshow(image2)
image3 = change_alpha(image,0.5)
ax = fig.add_subplot(223)
ax.imshow(image3)
image4 = change_alpha(image,2)
ax = fig.add_subplot(224)
ax.imshow(image4)
plt.show()          #显示绘制图像