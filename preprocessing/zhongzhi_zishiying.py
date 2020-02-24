import cv2
import numpy as np


img = cv2.imread('/media/lc/8A986A3C986A26C3/model/data/m4.png')
x, y, n = img.shape

# 参数设置
min_size = int(1)         # 滤波窗口的最小尺寸，一般为奇数
max_size = int(7)         # 滤波窗口的最大尺寸，一般为奇数
pading = int((max_size - 1) / 2)　  # 根据最大滤波窗口尺寸给图像添加边界



 


# 边界0填充,倒影填充
img_pading = cv2.copyMakeBorder(img,pading,pading,pading,pading,cv2.BORDER_DEFAULT,value=0)


cv2.imshow('add pading',img_pading)
cv2.waitKey(0)