#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8
from std_msgs.msg import UInt16

rospy.init_node('keypressed', anonymous=True)

pub = rospy.Publisher('dkey', Int8, queue_size=10)

def listener():
    rospy.Subscriber("/keyboard/keydown", UInt16, callback)

    #rospy.init_node('keypressed', anonymous=True)
    rate = rospy.Rate(10) #10 hz

   # rospy.loginfo("Talker node started...")

    while not rospy.is_shutdown():
        rate.sleep()
    #    pressed_int = 1
     #   pub.publish(pressed_int)
      #  rate.sleep()

def callback(data):
    print(data.data, data)
    if data.data == 100:
        pub.publish(1)

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass    
