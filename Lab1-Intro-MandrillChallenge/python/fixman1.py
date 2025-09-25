import cv2
import numpy as np

threshold = 128

BLUE = 0
GREEN = 1
RED = 2

highlight = RED
# load image from a file into the container
image = cv2.imread("images/mandrill1.jpg", cv2.IMREAD_UNCHANGED)

height, width, colour = image.shape

# temp = image
# for i in range(height):
#     for j in range(width):
#         temp[(i+32)%512,(j+32)%512,2] = image[i,j,2]
#         temp[i,j,0] = 0
#         temp[i,j,1] = 0 

b, g, r = cv2.split(image)

M = np.float32([
	[1, 0, 32],
	[0, 1, 32]
])

r = cv2.warpAffine(r, M, (width, height))

temp = cv2.merge((b,g,r))
# for i in range(height):
#     for j in range(width):
#         if image[i,j,highlight] < threshold:
#             #loop through 3 channels
#             for k in range(3):
#                 image[i,j,k] = 0
#         else:
#             #loop through 3 channels
#             for k in range(3):
#                 if k == highlight:
#                     image[i,j,k] = 255
#                 else:
#                     image[i,j,k] = 0



# save image to file
cv2.imwrite("python/fixman1.jpg", temp)