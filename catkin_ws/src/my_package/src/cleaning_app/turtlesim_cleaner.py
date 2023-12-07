#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time

# Initialize x and y in the global scope
x = 0.0
y = 0.0
yaw = 0.0

def location_callback(msg):
    global x, y, yaw
    x=msg.x
    y=msg.y
    yaw= msg.theta
    

def move_in_straight_line(velocity_publisher, speed, distance, is_forward):
    global x, y
    #get current location
    x0=x
    y0=y
    
    #declare message 
    velocity_message=Twist()

    if is_forward:
       velocity_message.linear.x=abs(speed)
    else:
        velocity_message.linear.x=-abs(speed)   

    moved_distance=0.0
    loop_rate= rospy.Rate(10) # publish 10 times per second

    while moved_distance < distance:
         rospy.loginfo("Turtle moves forward")
         velocity_publisher.publish(velocity_message)
         loop_rate.sleep()
         moved_distance = abs(math.sqrt(((x-x0)**2)+((y-y0)**2)))
         print("Moved Distance:", moved_distance)
         print("Current x:", x)
         
         
    #stop the robot
    velocity_message.linear.x=0.0
    velocity_publisher.publish(velocity_message)
    rospy.loginfo("Motion completed")

def rotate(velocity_publisher, angular_speed_degree, orientation_degree, is_clockwise):

    #declare msg
    msg=Twist()
    #turn to radian
    angular_speed= math.radians(abs(angular_speed_degree)) 
    #identify speed direction
    if (is_clockwise):
        msg.angular.z=-abs(angular_speed)
    else:
        msg.angular.z=abs(angular_speed)    

    loop_rate= rospy.Rate(10)
    angle_moved = 0.0
    t0=rospy.Time.now().to_sec()
    
    while(angle_moved<orientation_degree):
        print('turtle rotates')
        velocity_publisher.publish(msg)
        t1=rospy.Time.now().to_sec()
        loop_rate.sleep()
        angle_moved=(t1-t0)*angular_speed_degree
        print("Moved angle:", angle_moved)
        
         
         
    #stop the robot
    msg.angular.z=0.0
    velocity_publisher.publish(msg)
    rospy.loginfo("rotation completed")

def go_to_goal(velocity_publisher, x_goal, y_goal):
    
    global x, y, yaw
    k_linear=0.5
    k_angular=4.0

    #declare message
    velocity_msg=Twist()
    loop_rate= rospy.Rate(10)
    while(True):

         #get linear velocity 
         distance=abs(math.sqrt(((x_goal-x)**2) + ((x_goal-x)**2)))
         linear_velocity=k_linear*distance
         velocity_msg.linear.x=linear_velocity

         #get angular velocity
         angle=math.atan2(y_goal-y, x_goal-x)
         angular_velocity=k_angular*(angle - yaw)
         velocity_msg.angular.z=angular_velocity

         print('turtle is walking')
         velocity_publisher.publish(velocity_msg)
         loop_rate.sleep()

         print("Moved distance:", distance)
         print('current x :',x )
         print('current y :',y )
         
         if (distance <0.01):
            break
        
         
         
    #stop the robot
    velocity_msg.linear.x=0.0
    velocity_msg.angular.z=0.0
    velocity_publisher.publish(velocity_msg)
    rospy.loginfo("turtle reached")


def set_desired_orientaton(velocity_publisher, angular_speed_degree, desired_orientation_degree):
    orientation_degree=math.radians(desired_orientation_degree)-yaw
    clockwise=0
    if(orientation_degree<0):
        clockwise=1

    print ("orientation_angle_radians: ",math.degrees(orientation_degree))
    print ("desired_angle_degree: ",desired_orientation_degree)
    rotate(velocity_publisher,angular_speed_degree,math.degrees(orientation_degree),clockwise)

def spiral_clean(velocity_publisher, k_L, k_A):
    velocity_msg=Twist()
    loop_rate=rospy.Rate(1)
    while((x<10.5) and (y<10.5)):
        k_L+=1
        velocity_msg.linear.x=k_L
        velocity_msg.linear.y=0.0
        velocity_msg.linear.z=0.0
        velocity_msg.angular.x=0.0
        velocity_msg.angular.y=0.0
        velocity_msg.angular.z=k_A
        velocity_publisher.publish(velocity_msg)
        loop_rate.sleep()

    velocity_msg.angular.z=0.0
    velocity_msg.linear.x=0.0
    velocity_publisher.publish(velocity_msg)

def grid_clean(publisher, x_init, y_init):

    go_to_goal(publisher, x_init,y_init)
 
    set_desired_orientaton(publisher, 30, 0)
 
    for i in range(5):
        move_in_straight_line(publisher, 2.0, 1.0, True)
        rotate(publisher, 20, 90, False)
        move_in_straight_line(publisher, 2.0, 9.0, True)
        rotate(publisher, 20, 90, True)
        move_in_straight_line(publisher, 2.0, 1.0, True)
        rotate(publisher, 20, 90, True)
        move_in_straight_line(publisher, 2.0, 9.0, True)
        rotate(publisher, 20, 90, False)
    pass


if __name__ == "__main__":
    rospy.init_node('turtle_motion', anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10 )  
    
    rospy.Subscriber('/turtle1/pose',Pose, location_callback)
    time.sleep(2)
    #move_in_straight_line(velocity_publisher, 1.0, 7.0, True)  
    #rotate(velocity_publisher, 30, 180, False)
    #go_to_goal(velocity_publisher, 1.0, 1.0)
    #set_desired_orientaton(velocity_publisher,30,90)
    #spiral_clean(velocity_publisher, 0, 2)
    x_init= rospy.get_param("x_init")
    y_init= rospy.get_param("y_init")
    grid_clean(velocity_publisher, x_init, y_init)