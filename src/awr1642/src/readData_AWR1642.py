from __future__ import division
import serial
import time
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import os
import csv


gestureName="waving"
cwd = os.getcwd()
captureDir=cwd+"/capture_results/"
lst = os.listdir(captureDir)
number_of_frames=len(lst)
frameList=[]

for i in range(number_of_frames):
	frameNumber=str(i)
	data=np.load(captureDir+gestureName+frameNumber+".npy")

	dataItem=data.item(0)
	frameList.append(dataItem)
	#print(frameList[-1]['peakVal'])
