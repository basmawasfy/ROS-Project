#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

#create cvbridge object
bridge=CvBridge()

#define image callback function
def img_callback(ros_img):
   print('image is receives')
   #convert ros_img to openCV format
   try:
      cv_img=




#main function
def main(args):
    #ros node with name image_converter
    rospy.init_node('image_converter', anonymous=True)

    #subscribes to topic and excute callback when image is received

    #for turtlebot3 waffle     #image_topic="/camera/rgb/image_raw/compressed"
    #for usb cam               #image_topic="/usb_cam/image_raw"
    img_sub=rospy.Subscriber("/usb_cam/image_raw", Image, img_callback)

    try:
      rospy.spin()
    except KeyboardInterrupt:
      print("Shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)