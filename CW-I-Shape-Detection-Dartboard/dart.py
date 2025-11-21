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
import re

class Box:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


# LOADING THE IMAGE
# Example usage: python filter2d.py -n car1.png
parser = argparse.ArgumentParser(description='face detection')
parser.add_argument('-name', '-n', type=str)
args = parser.parse_args()

# /** Global variables */
cascade_name = "Dartboardcascade/cascade.xml"

# 2. Load the Strong Classifier in a structure called `Cascade'
model = cv2.CascadeClassifier()
if not model.load(cascade_name): # if got error, you might need `if not model.load(cv2.samples.findFile(cascade_name)):' instead
    print('--(!)Error loading cascade model')
    exit(0)


def detectAndDisplay(frame):
    detectedList = []
	# 1. Prepare Image by turning it into Grayscale and normalising lighting
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    # 2. Perform Viola-Jones Object Detection
    darts = model.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=3, flags=0, minSize=(20,20), maxSize=(210,210))
    # 3. Print number of Darts found
    # print(len(darts))
    # 4. Draw box around darts found
    for i in range(0, len(darts)):
        start_point = (darts[i][0], darts[i][1])
        end_point = (darts[i][0] + darts[i][2], darts[i][1] + darts[i][3])
        colour = (0, 255, 0)
        thickness = 2
        frame = cv2.rectangle(frame, start_point, end_point, colour, thickness)
        detectedList.append(Box(darts[i][0], darts[i][1], darts[i][2], darts[i][3]))

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
            img_name = content_list[4]
            x = float(content_list[0])
            y = float(content_list[1])
            width = float(content_list[2])
            height = float(content_list[3])
            x= int(x)
            y= int(y)
            width= int(width)
            height= int(height)
            # print(img_name in imageName)
            # print(imageName[14:17], img_name)
            if img_name in imageName:
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

def F1(FN, FP, TP):
    if TP != 0:

        recall = TP / (TP + FN) # aka TPR

        precision = TP / (TP + FP)

        return 2*precision*recall/(precision+recall)
    else:
        return None

def evaluateImage(imageName):
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





    # 3. Detect Darts and Display Result
    detectedList = detectAndDisplay( frame )
    groundTruthList = readGroundtruth(imageName, frame)

    FN, FP, TP = computeScores(detectedList,groundTruthList,0.2)
    print(FN, FP, TP)

    # 4. Save Result Image
    index = re.findall(r"\d+", imageName)[0]
    cv2.imwrite( "Results/detected"+str(index)+".jpg", frame )


    F1score = F1(FN, FP, TP)
    if F1score:
        print(F1score)
    else:
        print("No True Positives")

    return FN, FP, TP



# ==== MAIN ==============================================

imageName = args.name



if imageName == None:
    dirName = "./Dartboard/"
    totalFN = totalFP = totalTP = 0
    for i, _ in enumerate(os.listdir(dirName)):
        # print(i)
        imageName = dirName + "dart" + str(i) +".jpg"
        FN, FP, TP = evaluateImage(imageName)
        totalFN += FN
        totalFP += FP
        totalTP += TP
    
    
    combinedF1 = F1(totalFN, totalFP, totalTP)
    if combinedF1:
        print("combined F1:", combinedF1)
    else:
        print("No True Positives")
    
        
else:
    evaluateImage(imageName)
    