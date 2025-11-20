################################################
#
# COMS30068 - face.py
# University of Bristol
#
################################################

import numpy as np
import cv2
import os
import sys
import argparse

class Box:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


# LOADING THE IMAGE
# Example usage: python filter2d.py -n car1.png
parser = argparse.ArgumentParser(description='face detection')
parser.add_argument('-name', '-n', type=str, default='images/face1.jpg')
args = parser.parse_args()

# /** Global variables */
cascade_name = "frontalface.xml"


def detectAndDisplay(frame):
    detectedList = []
	# 1. Prepare Image by turning it into Grayscale and normalising lighting
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    # 2. Perform Viola-Jones Object Detections
    faces = model.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=7, flags=0, minSize=(10,10), maxSize=(300,300))
    # 3. Print number of Faces found
    print(len(faces))
    # 4. Draw box around faces found
    for i in range(0, len(faces)):
        start_point = (faces[i][0], faces[i][1])
        end_point = (faces[i][0] + faces[i][2], faces[i][1] + faces[i][3])
        colour = (0, 255, 0)
        thickness = 2
        frame = cv2.rectangle(frame, start_point, end_point, colour, thickness)
        detectedList.append(Box(faces[i][0], faces[i][1], faces[i][2], faces[i][3]))

    return detectedList


def iou(box1, box2):
    topLeftX = max(box1.x, box2.x)
    topLeftY = max(box1.y, box2.y)

    bottomRightX = min(box1.x+box1.w, box2.x+box2.w)
    bottomRightY = min(box1.y+box1.h, box2.y+box2.h)

    intersectedWidth = max(0, bottomRightX - topLeftX)
    intersectedHeight = max(0, bottomRightY - topLeftY)

    intersectionArea = intersectedWidth * intersectedHeight
    box1Area = box1.w * box1.h
    box2Area = box2.w * box2.h
    unionArea = box1Area + box2Area - intersectionArea
    
    if unionArea == 0:
        return 0
    return intersectionArea / unionArea


# ************ NEED MODIFICATION ************
def readGroundtruth(imageName, frame, filename='groundtruth.txt'):
    groundTruthList = []
    # read bounding boxes as ground truth
    with open(filename) as f:
        # read each line in text file
        for line in f.readlines():
            content_list = line.split(",")
            img_name = content_list[0]
            x = float(content_list[1])
            y = float(content_list[2])
            width = float(content_list[3])
            height = float(content_list[4])
            x= int(x)
            y= int(y)
            width= int(width)
            height= int(height)
            # print(imageName[7:12], img_name)
            if imageName[7:12] == img_name:
                # print(str(x)+' '+str(y)+' '+str(width)+' '+str(height))
                groundTruthList.append(Box(x, y, width, height))

                start_point = (x, y)
                end_point = (x+width, y+height)
                colour = (0, 0, 255)
                thickness = 2
                frame = cv2.rectangle(frame, start_point, end_point, colour, thickness)
    return groundTruthList

def computeScores(detectedList, groundTruthList, threshold=0.5):
    FN = 0
    FP = 0
    TP = 0

    matchedGroundTruthBoxes = set()

    for detectedBox in detectedList:
        bestGTIndex = -1
        bestIOU = 0

        # determine best ground truth corresponding to the detected box
        for i, groundTruthBox, in enumerate(groundTruthList):
            currIOU = iou(groundTruthBox, detectedBox)
            if currIOU > bestIOU:
                bestGTIndex = i
                bestIOU = currIOU
        # if the boxes overlap, check if ground truth already matched
        if bestIOU > threshold:
            if bestGTIndex not in matchedGroundTruthBoxes:
                matchedGroundTruthBoxes.add(bestGTIndex)
                TP += 1
            else:
                FP += 1
        else:
            FP += 1
    FN = len(groundTruthList) - len(matchedGroundTruthBoxes)
    return FN, FP, TP

        
    




# ==== MAIN ==============================================

imageName = args.name

# ignore if no such file is present.
if (not os.path.isfile(imageName)) or (not os.path.isfile(cascade_name)):
    print('No such file')
    sys.exit(1)

# 1. Read Input Image
frame = cv2.imread(imageName, 1)

# ignore if image is not array.
if not (type(frame) is np.ndarray):
    print('Not image data')
    sys.exit(1)


# 2. Load the Strong Classifier in a structure called `Cascade'
model = cv2.CascadeClassifier()
if not model.load(cascade_name): # if got error, you might need `if not model.load(cv2.samples.findFile(cascade_name)):' instead
    print('--(!)Error loading cascade model')
    exit(0)


# 3. Detect Faces and Display Result
detectedList = detectAndDisplay( frame )
groundTruthList = readGroundtruth(imageName, frame)

FN, FP, TP = computeScores(detectedList,groundTruthList,0.5)
print(FN, FP, TP)

recall = TP / (TP + FN) # aka TPR

precision = TP / (TP + FP)

F1 = 2*precision*recall/(precision+recall)

print(F1)

# 4. Save Result Image
cv2.imwrite( "detected.jpg", frame )


