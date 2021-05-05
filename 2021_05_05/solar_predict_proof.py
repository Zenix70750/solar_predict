import cv2  #导入opencv模块
import numpy as np


print("Hellow word!")     #打印“Hello word！”，验证模块导入成功

img = cv2.imread("predict.jpg")  #导入图片，图片放在程序所在目录
cv2.namedWindow("imagshow", 2)   #创建一个窗口
cv2.imshow('imagshow', img)    #显示原始图片

gauss = cv2.GaussianBlur(img, (3, 3), 2)  # 高斯模糊
gray=cv2.cvtColor(gauss,cv2.COLOR_BGR2GRAY) #转换为灰度图
hsv = cv2.cvtColor(gauss, cv2.COLOR_BGR2HSV)  # 转化成HSV图像
inRange_hsv = cv2.inRange(hsv, np.array([100, 43, 46]), np.array([124, 255, 255]))#紅色區域

retval,dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU) #使用大津算法进行图像二值化

#opening = cv2.morphologyEx(dst, cv2.MORPH_OPEN, (3,3))
#dilation = cv2.dilate(dst,(3,3),iterations = 3)

contours, hierarchy = cv2.findContours(dst.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros_like(dst)
count=0
for i in range(len(contours)):
    count+=1
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    
    if ( area > 3000):
        (x, y, w, h) = cv2.boundingRect(cnt)
        #if (w < 500) and (h < 500):  
        print("{}-area:{}".format(count,area),end="  ") #打印出每個板子的面積
        c_min = []
        c_min.append(cnt)
        cv2.drawContours(mask, c_min, -1, (255, 255, 255), thickness=-1)

cv2.namedWindow("mask", 2)   #创建一个窗口
cv2.imshow("mask", mask)
cv2.namedWindow("dst", 2)   #创建一个窗口
cv2.imshow("dst", dst)
cv2.namedWindow("hsv", 2)   #创建一个窗口
cv2.imshow("hsv", inRange_hsv)
#cv2.namedWindow("op", 2)   #创建一个窗口
#cv2.imshow("op", opening)
#cv2.namedWindow("di", 2)   #创建一个窗口
#cv2.imshow("di", dilation)



cv2.waitKey()