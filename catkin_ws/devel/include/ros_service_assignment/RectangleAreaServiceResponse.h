// Generated by gencpp from file ros_service_assignment/RectangleAreaServiceResponse.msg
// DO NOT EDIT!


#ifndef ROS_SERVICE_ASSIGNMENT_MESSAGE_RECTANGLEAREASERVICERESPONSE_H
#define ROS_SERVICE_ASSIGNMENT_MESSAGE_RECTANGLEAREASERVICERESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ros_service_assignment
{
template <class ContainerAllocator>
struct RectangleAreaServiceResponse_
{
  typedef RectangleAreaServiceResponse_<ContainerAllocator> Type;

  RectangleAreaServiceResponse_()
    : area(0.0)  {
    }
  RectangleAreaServiceResponse_(const ContainerAllocator& _alloc)
    : area(0.0)  {
  (void)_alloc;
    }



   typedef float _area_type;
  _area_type area;





  typedef boost::shared_ptr< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RectangleAreaServiceResponse_

typedef ::ros_service_assignment::RectangleAreaServiceResponse_<std::allocator<void> > RectangleAreaServiceResponse;

typedef boost::shared_ptr< ::ros_service_assignment::RectangleAreaServiceResponse > RectangleAreaServiceResponsePtr;
typedef boost::shared_ptr< ::ros_service_assignment::RectangleAreaServiceResponse const> RectangleAreaServiceResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator1> & lhs, const ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator2> & rhs)
{
  return lhs.area == rhs.area;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator1> & lhs, const ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ros_service_assignment

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ba46cd039de682077b3eaa09c3500c5c";
  }

  static const char* value(const ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xba46cd039de68207ULL;
  static const uint64_t static_value2 = 0x7b3eaa09c3500c5cULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_service_assignment/RectangleAreaServiceResponse";
  }

  static const char* value(const ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 area\n"
"\n"
"\n"
;
  }

  static const char* value(const ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.area);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RectangleAreaServiceResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_service_assignment::RectangleAreaServiceResponse_<ContainerAllocator>& v)
  {
    s << indent << "area: ";
    Printer<float>::stream(s, indent + "  ", v.area);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_SERVICE_ASSIGNMENT_MESSAGE_RECTANGLEAREASERVICERESPONSE_H
