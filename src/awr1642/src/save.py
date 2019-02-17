from __future__ import division
import serial
import time
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import os
import csv


# Name of input data from command line
gesture_name="waving"

# Get current working directory
training_data = os.getcwd()+"/training_data/"+gesture_name

# Remove exising training data from the directory gesture_name
try:  
    os.rmdir(training_data)
except OSError:  
    print ("The path %s" % training_data + " does not exist")
else:  
    print ("Successfully deleted the directory %s" % training_data)


# Create new folder and 
try:  
    os.mkdir(training_data)
except OSError:  
    print ("Creation of the directory %s failed" % training_data)
else:  
    print ("Successfully created the directory %s " % training_data)
