#彩色通道操作:红色通道与蓝色通道互换
from skimage import data,io
from matplotlib import pyplot as plt
#读入图像
image = data.coffee()
#分别取出红、绿、蓝三个颜色通道
image_r = image[:,:,0]
image_g = image[:,:,1]
image_b = image[:,:,2]
#红色蓝色互换
temp = image_r
image_r = image_b
image_b = temp
#将互换后的通道颜色重新赋给图像
image[:,:,0]=image_r
image[:,:,2] =image_b
#显示图像
plt.imshow(image)
plt.show()