import cv2
import numpy as np

threshold = 128

BLUE = 0
GREEN = 1
RED = 2

# highlight = BLUE
# load image from a file into the container
image = cv2.imread("mandrill0.jpg", cv2.IMREAD_UNCHANGED)

height, width, colour = image.shape

for i in range(height):
    for j in range(width):
        image[i,j,0], image[i,j,1], image[i,j,2] = image[i,j,2], image[i,j,0], image[i,j,1]

# save image to file
cv2.imwrite("fixman0.jpg", image)