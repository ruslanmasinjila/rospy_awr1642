#! /usr/bin/env python


################## ROS IMPORTS #########################
from __future__ import division
import rospy
import roslib; 
import sys 
from std_msgs.msg import *
from sensor_msgs.msg import *
from sensor_msgs.point_cloud2 import *
import pcl_ros as pcl

################## NUMPY AND MATPLOTLIB #########################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Future Imports
# from matplotlib.pyplot import *
# from numpy import *
# from time import *



class awr1642():

	def __init__(self):
		print "awr1642 running..."
		self.pointCloud2_subscriber=rospy.Subscriber("/mmWaveDataHdl/RScan",PointCloud2,self.pointCloud2_cb)
	
		# coordinates of detected objects
		self.xCoordinates=[]
		self.yCoordinates=[]



	def pointCloud2_cb(self,pointCloud2_data):

		cloud= list(read_points(pointCloud2_data,field_names = ("x", "y","z","intensity")))
		self.invisibleCube(cloud)
		print cloud


	def invisibleCube(self,points):

 		xNear=0.25
		xFar=0.75
		yNegative=-0.25
		yPositive=0.25

		
		count=0
		for i in points:
			if i[0]>=xNear and i[0]<=xFar and i[1]>=yNegative and i[1]<=yPositive:

				count=count+1
				self.xCoordinates.append(i[0])
				self.yCoordinates.append(i[1])
		print count


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




	
