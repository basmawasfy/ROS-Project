#!/usr/bin/env python 

import numpy as np
import cv2

#create a black image with dimentions 512 *512 and 3 color channel 
img=np.zeros((512, 512, 3), np.uint8)

#draw a white line starts from (0,0) till (511, 511) . and white(255, 255, 255). thickness is 5 pixels
cv2.line(img, (0,0), (511, 511), (255, 255, 255), 5)

#draw a green rectangle . top-left corner, bottom-right corner, color, thickness
cv2.rectangle(img, (386, 0), (510, 135), (0, 255, 0), 3)

#draw solid red eclipse with center(256, 256), major, minor axes are 100, 50 pixels, the elipse spans from 0->180, color, solid fill=-1
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)

#draw a yellow polygon , true -> closed shape
pts=np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255))

# add text , font sze = 4, thickness = 2
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 2)


cv2.imshow("image panel" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()


