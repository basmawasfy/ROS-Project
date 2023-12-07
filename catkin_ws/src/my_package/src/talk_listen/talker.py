#!/usr/bin/env python
import rospy
from  std_msgs.msg import String

def talker():
    # create node
    rospy.init_node('talker',anonymous=True)

    # publisher object
    pub=rospy.Publisher('chatter', String, queue_size=10)

    #freq
    rate=rospy.Rate(10)
    #code
    i=0
    while not rospy.is_shutdown():
        name="basma wasfy %s" %i
        # publishing 
        pub.publish(name)
        rate.sleep()
        i+=1

if __name__ == '__main__' :
    try:
        talker()
    except rospy.ROSInterruptException:
        pass    