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

# LOADING THE IMAGE
# Example usage: python convolution.py -n car1.png

parser = argparse.ArgumentParser(description='Convert RGB to GRAY')
parser.add_argument('-name', '-n', type=str, default='car1.png')
args = parser.parse_args()

# ==================================================
def MedianFilter(input, size):

	# intialise the output using the input
	output = np.zeros([input.shape[0], input.shape[1]], dtype=np.float32)
	
	# CREATING A DIFFERENT IMAGE kernel WILL BE NEEDED
	# TO PERFORM OPERATIONS OTHER THAN GUASSIAN BLUR!!!
	
	# we need to create a padded version of the input
	# or there will be border effects
	kernelRadius = round(( size - 1 ) / 2)
	paddedInput = cv2.copyMakeBorder(input, 
		kernelRadius, kernelRadius, kernelRadius, kernelRadius, 
		cv2.BORDER_REPLICATE)

	# now we can do the convoltion
	for i in range(0, input.shape[0]):	
		for j in range(0, input.shape[1]):
			patch = paddedInput[i:i+size, j:j+size]
			median = np.median(patch)
			
			output[i, j] = median

	return output

# ==== MAIN ==============================================
imageName = args.name

# ignore if no such file is present.
if not os.path.isfile(imageName):
    print('No such file')
    sys.exit(1)

# Read image from file
image = cv2.imread(imageName, 1)

# ignore if image is not array.
if not (type(image) is np.ndarray):
    print('Not image data')
    sys.exit(1)

# CONVERT COLOUR, BLUR AND SAVE
gray_image = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
gray_image = gray_image.astype(np.float32)

# apply Gaussian blur
carMedianFiltered = MedianFilter(gray_image,5)

# save image
cv2.imwrite( "output/car2-median.jpg", carMedianFiltered )