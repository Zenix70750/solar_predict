import cv2
import numpy as np

img = cv2.imread('predict3.JPG')

gauss = cv2.GaussianBlur(img, (3, 3), 0)  # 高斯模糊
gray = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY)


canny = cv2.Canny(gray, 60, 255 )
closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, (3,3))

ret, thresh = cv2.threshold(gray, 150,255, cv2.THRESH_OTSU)

erosion = cv2.erode(thresh.copy(),(3,3),iterations = 7)

contours, hierarchy = cv2.findContours(erosion.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros_like(erosion)
count=0
for i in range(len(contours)):
    count+=1
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    
    if (18000 < area < 20000):
        (x, y, w, h) = cv2.boundingRect(cnt)
        #if (w < 500) and (h < 500):  
        print("{}-area:{}".format(count,area),end="  ") #打印出每個板子的面積
        c_min = []
        c_min.append(cnt)
        cv2.drawContours(mask, c_min, -1, (255, 255, 255), thickness=-1)
        
        
        


cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
cv2.imshow('mask', mask)
cv2.namedWindow('closing', cv2.WINDOW_NORMAL)
cv2.imshow('closing', closing)
#cv2.namedWindow('dilation', cv2.WINDOW_NORMAL)
#cv2.imshow('dilation', dilation)
cv2.namedWindow('erosion', cv2.WINDOW_NORMAL)
cv2.imshow('erosion', erosion)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
#cv2.namedWindow('canny', cv2.WINDOW_NORMAL)
#cv2.imshow('canny', canny)
#cv2.namedWindow('thresh', cv2.WINDOW_NORMAL)
#cv2.imshow('thresh', thresh)
cv2.waitKey(0)