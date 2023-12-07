#!/usr/bin/env python 

import numpy as np
import cv2

print ('read an image from file')
color_image = cv2.imread("images/flower.jpg",cv2.IMREAD_COLOR)

print ('display image in native color')
cv2.imshow("Original Image",color_image)
cv2.moveWindow("Original Image",0,0)
print(color_image.shape)

height,width,channels = color_image.shape

print ('slipt the image into three channels.')
blue,green,red = cv2.split(color_image)

cv2.imshow("Blue Channel",blue)
cv2.moveWindow("Blue Channel",0,height)


cv2.imshow("Red Channel",red)
cv2.moveWindow("Red Channel",0,height)


cv2.imshow("Greeen Channel",green)
cv2.moveWindow("Green Channel",0,height)

hsv_image=cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
h, s, v= cv2.split(hsv_image)

hsv = np.concatenate((h,s,v),axis=1)
cv2.imshow("hsv_image",hsv_image)
cv2.imshow("hsv",hsv)

gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image ",gray_image)

cv2.waitKey(0)  # Wait for any key press
cv2.destroyAllWindows()  # Close the window

