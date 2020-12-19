import numpy as np
from scipy import signal
from skimage import data
from matplotlib import pyplot as plt
# 定义二维灰度图像的空间滤波函数
def correl2d(img,window):
    #使用滤波器实现图像的空间相关
    # mode = 'same' 表示输出尺寸等于输入尺寸
    # biundary = 'fill' 表示滤波前，用常量值填充原始图像的边缘，默认常量值为0
    s = signal.correlate2d(img, window, mode = 'same', boundary='fill')
    return s.astype(np.uint8)
# img为原始图像
img = data.camera()
# 3x3 盒状滤波模板
window1 = np.ones((3, 3))/(3 ** 2)
# 5x5 盒状滤波模板
window2 = np.ones((5, 5))/(5 ** 2)
# 9x9 盒状滤波模板
window3 = np.ones((9, 9))/(9 ** 2)
# 生成滤波结果
new_img1 = correl2d(img,window1)
new_img2 = correl2d(img,window2)
new_img3 = correl2d(img,window3)
# 显示图像
plt.figure()
# 显示原始图像
plt.imshow(img, cmap = 'gray')
plt.figure()
# 显示 3x3 盒状滤波结果
plt.imshow(new_img1, cmap = 'gray')
plt.figure()
# 显示 5x5 盒状滤波结果
plt.imshow(new_img2, cmap = 'gray')
plt.figure()
# 显示 9x9 盒状滤波结果
plt.imshow(new_img3, cmap = 'gray')
