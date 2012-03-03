#!/usr/bin/python
"""
  Publishes random PoseArray for tviz to display.
"""
import roslib; roslib.load_manifest('ps7_rviz')
import rospy
import tf
import time


from geometry_msgs.msg import PoseArray, Pose, Point, Quaternion
from random import random

pub = rospy.Publisher('particles', PoseArray)
rospy.init_node('ps7_random_example')

while not rospy.is_shutdown():
  poses = PoseArray()
  poses.header.frame_id = "map"
  poses.header.stamp = rospy.Time.now()

  for i in range(5000):
    point = Point(random()*54, random()*11, 0)
    direction = random() * 2 * 3.14
    quat = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, direction ))
    poses.poses.append(Pose(point, quat))

  pub.publish(poses)
  time.sleep(1/30)

