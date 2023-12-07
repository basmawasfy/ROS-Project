#!/usr/bin/env python
import rospy
from my_package.msg import IoTSensor
#callback funtion
def IoT_data_calback(message):
    rospy.loginfo("new iot data received : (%d, %s, %.2f, %.2f)", message.id, message.name, message.humidity, message.temperature)

def subscriber():

    #create node 
    rospy.init_node("subscriber_node", anonymous=True)
    #subscriber object
    rospy.Subscriber("sensor_data", IoTSensor, IoT_data_calback)
    # keep listening
    rospy.spin()

    
if __name__=="__main__":
    subscriber()
