#!/usr/bin/env python
import rospy
from std_msgs.msg import String

# callback definition
def chatter_callback(message):
       print("WELCOME ", message.data)

def listener():
   # create node 
   rospy.init_node('listener', anonymous=True)

   # subscriber object
   rospy.Subscriber('chatter', String, chatter_callback)

   # keap listening
   rospy.spin()     


if __name__ =='__main__':
    listener()
    