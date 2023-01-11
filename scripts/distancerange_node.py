#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64, String

rospy.init_node('distancerange', anonymous=True)

pub = rospy.Publisher('distrange', String, queue_size=10)

def listener():
    rospy.Subscriber("/chatter", Float64, callback)

    rate = rospy.Rate(10) #10 hz

    while not rospy.is_shutdown():
        rate.sleep()


def callback(data):
    dist = data.data
    if dist < 5:
        pub.publish("close")
    else:
        if dist < 10:
            pub.publish("mid-range")
        else:
            pub.publish("far")

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass    
