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

def convolution(input, kernel):
    output = np.zeros([input.shape[0], input.shape[1]], dtype=np.float32)
    
    kernelRadiusX = round(( kernel.shape[0] - 1 ) / 2)
    kernelRadiusY = round(( kernel.shape[1] - 1 ) / 2)
    paddedInput = cv2.copyMakeBorder(input, kernelRadiusX, kernelRadiusX, kernelRadiusY, kernelRadiusY, cv2.BORDER_REPLICATE)
    # rotatedKernel = kernel[::-1][::-1]
    for i in range(0, input.shape[0]):
        for j in range(0, input.shape[1]):
            # patch = paddedInput[i:i+kernel.shape[0], j:j+kernel.shape[1]]
            sum = 0.0
            for m in range(-kernelRadiusX, kernelRadiusX+1):
                for n in range(-kernelRadiusY, kernelRadiusY+1):
                    # find the correct indices we are using
                    imagex = i + m + kernelRadiusX
                    imagey = j + n + kernelRadiusY
                    kernelx = m + kernelRadiusX
                    kernely = n + kernelRadiusY
                    # get the values from the padded image and the kernel
                    imageval = paddedInput[imagex, imagey]
                    kernalval = kernel[kernelx, kernely]
                    # do the multiplication
                    sum += imageval * kernalval	
            # print(sum)
            if np.sum(kernel) != 0:
                sum /= np.sum(kernel)
            output[i,j] = sum

    return output



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

# apply convolution

# carBlurred = GaussianBlur(gray_image,23);
lowPassKernel = np.array([  [1,1,1],
                            [1,1,1],
                            [1,1,1]])

highPassKernel = np.array([ [0,-1,0],
                            [-1,5,-1],
                            [0,-1,0]])

horizontalEdgeKernel = np.array([   [-1,-2,-1],
                                    [0,0,0],
                                    [1,2,1]])

verticalEdgeKernel = np.array([ [-1,0,1],
                                [-2,0,2],
                                [-1,0,1]])

horizontalEdgeConvolvedCar = convolution(gray_image,horizontalEdgeKernel)
verticalEdgeConvolvedCar = convolution(gray_image,verticalEdgeKernel)
highPassConvolvedCar = convolution(gray_image,highPassKernel)
lowPassConvolvedCar = convolution(gray_image,lowPassKernel)

# save image
cv2.imwrite( "output/manual-convo-horizontal.jpg", horizontalEdgeConvolvedCar )
cv2.imwrite( "output/manual-convo-vertical.jpg", verticalEdgeConvolvedCar )
cv2.imwrite( "output/manual-convo-high.jpg", highPassConvolvedCar )
cv2.imwrite( "output/manual-convo-low.jpg", lowPassConvolvedCar )