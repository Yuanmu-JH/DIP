#设置显示的中文字体，使其可以在图表中显示中文
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"C:\Windows\Fonts\STFANGSO.ttf",size =12)
#相加减工作
from skimage import data
from matplotlib import pyplot as plt
moon = data.moon()
camera = data.camera()
image_minus = moon-camera
image_plus = moon+camera
plt.set_cmap(cmap='gray')
plt.subplot(2,2,1)
plt.title('月亮图像',fontproperties=font_set)
plt.imshow(moon)
plt.subplot(2,2,2)
plt.title('摄影师图像',fontproperties=font_set)
plt.imshow(camera)
plt.subplot(2,2,3)
plt.title('月亮＋摄影师',fontproperties=font_set)
plt.imshow(image_plus)
plt.subplot(2,2,4)
plt.title('月亮-摄影师',fontproperties=font_set)
plt.imshow(image_minus)
plt.show()