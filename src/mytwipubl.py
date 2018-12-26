#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('twistpup')
pub=rospy.Publisher('cmd_vel',Twist,queue_size=10)

rate=rospy.Rate(2)

twi=Twist()
twi.linear.x=2.3
twi.angular.z=0.6
while not rospy.is_shutdown():
    pub.publish(twi)
    
    rate.sleep()