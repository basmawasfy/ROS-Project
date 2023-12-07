#!usr/bin/env python
import rospy
import sys
from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

def RectangleArea_client(w, h):
    rospy.wait_for_service('rectangleArea')
    try:
       s_obj=rospy.ServiceProxy('rectangleArea',RectangleAreaService )
       response= s_obj(w, h)
       return response.area 
    except rospy.ServiceException(e):
        print("Service call failed: %s "%e)




if __name__ == "__main__":
    if len(sys.argv) == 3:
        w= int(sys.argv[1])
        h= int(sys.argv[2])
    else:
        print("%s [w h]"%sys.argv[0])
        sys.exit(1)   
    print("Requsting [ %s * %s]"%(w, h))   
    r_area=RectangleArea_client(w, h)
    print("%s * %s = %s"%(w, h, r_area))  
