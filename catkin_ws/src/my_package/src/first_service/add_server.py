#!/usr/bin/env python
from my_package.srv import AddtwoIntsRequest
from my_package.srv import AddtwoIntsResponse
from my_package.srv import AddtwoInts

import rospy

#callback function
def handle_add_two_ints(request):
    print("Returning [%s + %s = %s]"%(request.a, request.b, (request.a+request.b)))
  
    # return response function from respons file     
    return AddtwoIntsResponse(request.a+request.b)

# (server function) 
def add_two_ints_server():
    #node
    rospy.init_node('add_two_int_server')
    #create new ros service
    s=rospy.Service('add_two_ints', AddtwoInts, handle_add_two_ints)
    
    print ("Ready to add two ints.")
    #keep node running
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()    