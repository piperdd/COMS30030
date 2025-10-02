################################################
#
# COMS30068 - convolution.py
# TOPIC: create, save and display an image
#
# Getting-Started-File for OpenCV
# University of Bristol
#
################################################

import numpy as np
import cv2
import os
import sys
import argparse
import glob

# LOADING THE IMAGE
# Example usage: python convolution.py -n car1.png

parser = argparse.ArgumentParser(description='Convert RGB to GRAY')
parser.add_argument('-dirname', '-d', type=str, default='')
parser.add_argument('-extname', '-e', type=str, default='png')
args = parser.parse_args()

# ==== MAIN ==============================================

# initial long exposure image
longexposureimg = 0
n = 0
# read each image in the folder

for file in glob.glob(os.path.join(args.dirname, "*." + args.extname)):
	# Read image from file
	image = cv2.imread(file, 1).astype(np.float32)
	# print(image.shape)
	longexposureimg += image
	n += 1
longexposureimg /= n


# save image
cv2.imwrite( "output/longexposureimg.jpg", longexposureimg )





