#!/usr/bin/env python
import rospy
#import messages type 
from  turtlesim.msg import Pose
from  geometry_msgs.msg import Twist
import math
import time
from std_srvs.srv import Empty

x=0
y=0
z=0
theta=0

# callback definition
def location_callback(message):
    
    print ("pose callback")
    print ("x = {}".format(message.x)) #in python3
    print ("y = %f" %message.y)
    print ("theta =%f" %message.theta) #in python2

def move(speed, distance):
    # declare twist message to send velocity commands
    velocity_msg=Twist()
    #get current location from the global variable before entering loop
    x0=x
    y0=y
    #z0=z
    #theta0=theta
    
    #assign the x coordinate of linear velocity to the speed
    velocity_msg.linear.x = speed 
    distance_moved =0.0
    #we publish the velocity at 10 Hz (10 times a second)
    loop_rate=rospy.Rate(10)
    #create a publisher for the velocity message on the appropriate topic
    velocity_publisher=rospy.Publisher('turtle1/cmd_vel',Twist, queue_size=10) 

    while True:
        rospy.loginfo("Turtlesim moves forwards")
        # publishing 
        velocity_publisher.publish(velocity_msg)  

        loop_rate.sleep()
        # measure the distance moved
        distance_moved+=abs(0.5*math.sqrt(((x-x0)**2)+((y-y0)**2))) 
        print(distance_moved)
        if not (distance_moved<distance):
            rospy.loginfo("reached")
            break
        #finally, stop the robot when the distance is moved
        velocity_msg.linear.x =0
        velocity_publisher.publish(velocity_msg)

if __name__ == '__main__' :
    try:
        # create subscriber node 
        rospy.init_node('get_location', anonymous=True)
        #declare velocity publisher
        velocity_publisher=rospy.Publisher('turtle1/cmd_vel',Twist, queue_size=10) 
        # subscriber object (subscribe to the topic of the pose of turtlesim)
        rospy.Subscriber('turtle1/pose', Pose, location_callback)  
        

        time.sleep(2)
        print("move:")
        move(1.0,5.0)
        time.sleep(2)
        print("start reset:")
        rospy.wait_for_service("reset")
        reset_turtle=rospy.ServiceProxy("reset", Empty)
        reset_turtle()
        print ('end reset: ')

        # keep listening
        rospy.spin()     

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")    







