import cv2
import numpy as np

threshold = 128

# load image from a file into the container
image = cv2.imread("mandrill.jpg", cv2.IMREAD_UNCHANGED)

height, width = image.shape

for i in range(height):
    for j in range(width):
        if image[i,j] < threshold:
            # print("1")
            image[i,j] = 0
        else:
            # print("0")
            image[i,j] = 255


# save image to file
cv2.imwrite("threshold.jpg", image)