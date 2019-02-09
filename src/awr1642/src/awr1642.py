#! /usr/bin/env python


##################IMPORTS#########################
from __future__ import division
import rospy
import roslib; 
import sys 
from std_msgs.msg import *
from sensor_msgs.msg import *
from sensor_msgs.point_cloud2 import *
from pcl_ros import *

# Future Imports
# from matplotlib.pyplot import *
# from numpy import *
# from time import *


class awr1642():

	def __init__(self):
		print "awr1642 running..."
		self.pointCloud2_subscriber=rospy.Subscriber("/mmWaveDataHdl/RScan",PointCloud2,self.pointCloud2_cb)


	def pointCloud2_cb(self,pointCloud2_data):

		#print pointCloud2_data
		cloud= read_points(pointCloud2_data, skip_nans=False,field_names = ("x", "y"))

		points = []
		for pt in cloud:
			pt = list(pt)
			pt.append(1)
			points.append(pt)

		print points



def main():

	# Initialize node
	rospy.init_node("awr1642")
	print "awr1642 initialized..."

	# Create node
	awr1642_node=awr1642()

	# Continuous loop
	rospy.spin()


if __name__ == "__main__":
	main()




	
