#!/usr/bin/env python
import rospy
import random
from my_package.msg import IoTSensor
def subscriber():
    #create node
    rospy.init_node('publish_sensor_data', anonymous=True)
    #publisher object 
    pub=rospy.Publisher('sensor_data', IoTSensor,queue_size=10)
    #freq
    rate=rospy.Rate(10)
    #code
    i=0
    while not rospy.is_shutdown():
        iot_sensor=IoTSensor()
        iot_sensor.id=i
        iot_sensor.name='IoT_Sensor_01:'
        iot_sensor.humidity= 12.8+random.random()
        iot_sensor.temperature=34.8+random.random()
        rospy.loginfo("IoTSensor publish:")
        rospy.loginfo(iot_sensor)
        pub.publish(iot_sensor)
        rate.sleep()
        i+=1

if __name__ =="__main__":
    try:
        subscriber()
    except rospy.ROSInternalException:
        pass
        
