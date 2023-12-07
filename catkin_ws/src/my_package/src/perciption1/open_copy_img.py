#!/usr/bin/env python 
import numpy as np
import cv2

img_name = 'flower'

print("read an image from file")
img = cv2.imread("images/"+img_name+".jpg")

print("create a window holder for image")
cv2.namedWindow("image window", cv2.WINDOW_NORMAL)

print("display the image")
cv2.imshow("image window", img)

print("press a key inside the image to make a copy")
cv2.waitKey(0)

print("image copied")
cv2.imwrite("images/copy/"+img_name+"-copy.jpg",img)