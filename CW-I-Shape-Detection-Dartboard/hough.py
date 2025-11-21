import numpy as np
import cv2
import os
import sys
import argparse
import re

def normaliseAndOutput(filename, img):
    normalized = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite( filename, normalized )

def hough(gradientMagnitudeBinary, gradientDirection, minRadius, maxRadius):
    # initialize hough space
    numRow, numCol = gradientMagnitudeBinary.shape
    houghSpace = np.zeros((numRow, numCol, maxRadius - minRadius))

    for row, col in np.argwhere(gradientMagnitudeBinary):
        for r in range(minRadius, maxRadius):
            x0 = int(col + r * np.cos(gradientDirection[row,col]))
            y0 = int(row + r * np.sin(gradientDirection[row,col]))

            # accumulate votes
            if (0 <= x0 < numCol) and (0 <= y0 < numRow):
                houghSpace[y0, x0, r - minRadius] += 1

            x0 = int(col - r * np.cos(gradientDirection[row,col]))
            y0 = int(row - r * np.sin(gradientDirection[row,col]))

            # accumulate votes
            if (0 <= x0 < numCol) and (0 <= y0 < numRow):
                houghSpace[y0, x0, r - minRadius] += 1

    return houghSpace

def generateHoughSpace(imageName, minRadius=50, maxRadius=210):
    
    index = re.findall(r"\d+", imageName)[0]

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

    horizontalEdgeKernel = np.array([   [-1,-2,-1],
                                        [0,0,0],
                                        [1,2,1]])

    verticalEdgeKernel = np.array([ [-1,0,1],
                                    [-2,0,2],
                                    [-1,0,1]])

    horizontalEdgeConvolvedImg = cv2.filter2D(src=gray_image, ddepth=-1, kernel=horizontalEdgeKernel)
    verticalEdgeConvolvedImg = cv2.filter2D(src=gray_image, ddepth=-1, kernel=verticalEdgeKernel)

    magnitude = np.sqrt(verticalEdgeConvolvedImg**2 + horizontalEdgeConvolvedImg**2)
    magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    _, thresholdedMagnitude = cv2.threshold(magnitude, 80, 255, cv2.THRESH_BINARY)
    # normaliseAndOutput("hough/magnitude/"+str(index)+".jpg", thresholdedMagnitude)

    direction = np.arctan2(horizontalEdgeConvolvedImg,verticalEdgeConvolvedImg)
    # normaliseAndOutput("hough/direction.jpg", direction)

    magnitudeBinary = thresholdedMagnitude > 0
    houghSpace = hough(magnitudeBinary, direction, minRadius, maxRadius)

    print("hough space", index)
    np.save("hough/np/houghSpace"+str(index)+".npy", houghSpace)


def loadHoughSpace(imageName, threshold=30, minRadius=50):
    
    index = re.findall(r"\d+", imageName)[0]

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

    houghSpace = np.load("hough/np/houghSpace"+str(index)+".npy")
    circles = np.argwhere(houghSpace > threshold)

    circles = [(y,x,r+minRadius) for y, x, r in circles]

    print(len(circles))
    for circle in circles:
        y,x,r = circle
        cv2.circle(image, center=(x,y), radius=r, color=(0,255,0), thickness=2)

    cv2.imwrite("./hough/output/hough"+str(index)+".jpg", image)



# ==== MAIN ==============================================

parser = argparse.ArgumentParser(description='Convert RGB to GRAY')
parser.add_argument('-name', '-n', type=str)
args = parser.parse_args()

imageName = args.name

mode = "load"

threshold = 12
minRadius=50
maxRadius=210

if imageName == None:
    dirName = "./Dartboard/"
    if mode == "generate":
        for i, _ in enumerate(os.listdir(dirName)):
            imageName = dirName + "dart" + str(i) +".jpg"
            generateHoughSpace(imageName,minRadius,maxRadius)
    else:
        for i, _ in enumerate(os.listdir(dirName)):
            imageName = dirName + "dart" + str(i) +".jpg"
            loadHoughSpace(imageName,threshold,minRadius)
else:
    if mode == "generate":
        generateHoughSpace(imageName,minRadius,maxRadius)
    else:
        loadHoughSpace(imageName,threshold,minRadius)



# 


