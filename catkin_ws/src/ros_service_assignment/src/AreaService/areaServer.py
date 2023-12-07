#!usr/bin/env python
import rospy
from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

def areaService_callback(req):
    print("[%s * %s = %s]"%(req.width, req.height,(req.width * req.height)))
    return RectangleAreaServiceResponse(req.width * req.height)


def RectangleAreaServer():
    rospy.init_node('areaServer')
    new_S=rospy.service('rectangleArea', RectangleAreaService,areaService_callback )
    print("Ready to calculate Area ")
    rospy.spin()

if __name__ =="__main__":
    RectangleAreaServer()

