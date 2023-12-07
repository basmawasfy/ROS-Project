#!/usr/bin/env python
from my_package.srv import AddtwoIntsRequest
from my_package.srv import AddtwoIntsResponse
from my_package.srv import AddtwoInts
import sys
import rospy
# formulate and send a request
def add_two_ints_client(x, y):
    # wait till service is activated
    rospy.wait_for_service('add_two_ints')
    try:
       # creating the object
       add_two_ints_obj=rospy.ServiceProxy('add_two_ints', AddtwoInts)
       # sending the request
       resp1=add_two_ints_obj(x, y)
       return resp1.sum
    except rospy.ServiceException(e):
        print("Service call failed: %s"%e)
       


if __name__ == "__main__":
    if len(sys.argv)==3:
        x=int(sys.argv[1])
        y= int(sys.argv[2])
    else:
        print("%s [x y]" %sys.argv[0])
        sys.exit(1)
    print("Requesting %s + %s"%(x, y))
    s= add_two_ints_client(x, y)
    print("%s +%s = %s" %(x, y, s))

