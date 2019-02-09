#! /usr/bin/env python


##################IMPORTS#########################
from __future__ import division
import rospy
import sys
from std_msgs.msg import String
from std_msgs.msg import *
from math import *
from numpy import *


class awr1642():

	def __init__(self):
		print "awr1642 running..."



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




	
