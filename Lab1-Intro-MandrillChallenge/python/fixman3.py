import cv2
import numpy as np

threshold = 128

BLUE = 0
GREEN = 1
RED = 2

# highlight = BLUE
# load image from a file into the container
image = cv2.imread("images/mandrill3.jpg", cv2.IMREAD_UNCHANGED)

height, width, colour = image.shape

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for i in range(height):
    for j in range(width):
        for k in range(3):
            image[i,j,k] = 255 - image[i,j,k]

# save image to file
cv2.imwrite("python/fixman3.jpg", gray)