from skimage import io
from matplotlib import pyplot as plt    #导入绘图模块

file_name= 'Charapter1/test.jpg'
image=io.imread(file_name)
plt.imshow(image)   #进行图片绘制
plt.show()          #显示绘制图像