#! /usr/bin/env python


##################IMPORTS#########################
from __future__ import division
import rospy
import roslib; 
import sys 
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import *
from sensor_msgs.msg import *
#from point_cloud2 import *
from numpy import *
#from matplotlib.pyplot import *
from time import *


class awr1642():

	def __init__(self):
		print "awr1642 running..."
		self.pointCloud2_subscriber=rospy.Subscriber("/mmWaveDataHdl/RScan",PointCloud2,self.pointCloud2_cb)


	def pointCloud2_cb(self,pointCloud2_data):
		print pointCloud2_data



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




	
