#!/usr/bin/env python

###################################
# File for testing astar efficiency
###################################

import rospy
import time
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped


def main(init_x, init_y, end_x, end_y, start_pub, end_pub):
    start_point = PoseWithCovarianceStamped()
    start_point.header.frame_id = 'map'
    start_point.pose.pose.position.x = init_x
    start_point.pose.pose.position.y = init_y
    end_point = PoseStamped()
    end_point.header.frame_id = 'map'
    end_point.pose.position.x = end_x
    end_point.pose.position.y = end_y
    start_pub.publish(start_point)
    end_pub.publish(end_point)


if __name__ == '__main__':
    try:
        rospy.init_node('astar_test', anonymous=True)
        start_point_pub = rospy.Publisher('initialpose_test', PoseWithCovarianceStamped, queue_size=10)
        end_point_pub = rospy.Publisher('move_base_simple/goal_test', PoseStamped, queue_size=10)
        main(-8.804, 1.949, 1.386, -0.946, start_point_pub, end_point_pub)
    except rospy.ROSInterruptException:
        pass
