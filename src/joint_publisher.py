#!/usr/bin/env python3
from std_msgs.msg import Float64
import math

'''
Joint :

battery_joint
cover_joint
imu_joint
left_back_knee_joint
left_back_shoulder_joint
left_front_knee_joint
left_front_shoulder_joint
mainboard_joint
right_back_knee_joint
right_back_shoulder_joint
right_front_knee_joint
right_front_shoulder_joint
joint_state_controller
'''

def talker():
    pub = rospy.Publisher('/bittle/right_front_shoulder_joint/command', Float64, queue_size=10) # one publisher per joint
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        position = math.pi/2
        rospy.loginfo(position)
        pub.publish(position) #publish the calculate position to the on the '/bittle/right_front_shoulder_joint/command' publisher
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass