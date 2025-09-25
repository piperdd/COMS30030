import cv2
import numpy as np

threshold = 128

BLUE = 0
GREEN = 1
RED = 2

highlight = BLUE
# load image from a file into the container
image = cv2.imread("mandrillRGB.jpg", cv2.IMREAD_UNCHANGED)

height, width, colour = image.shape

for i in range(height):
    for j in range(width):
        if image[i,j,highlight] < threshold:
            #loop through 3 channels
            for k in range(3):
                image[i,j,k] = 0
        else:
            #loop through 3 channels
            for k in range(3):
                if k == highlight:
                    image[i,j,k] = 255
                else:
                    image[i,j,k] = 0



# save image to file
cv2.imwrite("colourthreshold.jpg", image)