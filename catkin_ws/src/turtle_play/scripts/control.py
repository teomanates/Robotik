#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#publisher node initialize
rospy.init_node("control_node")
pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=1)

#subscriber for pose
def callback(msg):
    print(msg)
    
rospy.Subscriber("/turtle1/pose", Pose, callback)


#msg for send by publisher
msg = Twist()

msg.linear.x = -1
msg.angular.z = -1

#while not rospy.is_shutdown():
#    pub.publish(msg)
#    rospy.sleep(1)
 
for i in range(5):
    pub.publish(msg)
    rospy.sleep(1)  
    
# rospy.spin()
