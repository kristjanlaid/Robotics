import os.path
from os import path
import numpy as np
import cv2

trackbar_value_lH = 0
trackbar_value_lS = 0
trackbar_value_lV = 0
trackbar_value_hH = 125
trackbar_value_hS = 125
trackbar_value_hV = 125

if path.exists('trackbar_defaults.txt'):
    values = open('trackbar_defaults.txt', 'r')
    trackbar_value_lH = int(values.readline())
    trackbar_value_lS = int(values.readline())
    trackbar_value_lV = int(values.readline())
    trackbar_value_hH = int(values.readline())
    trackbar_value_hS = int(values.readline())
    trackbar_value_hV = int(values.readline())

    values.close()


cap = cv2.VideoCapture(0)

old_time = 0
new_time = 0

cv2.namedWindow("Original")

def updateValue_lH(new_value_lH):
    global trackbar_value_lH
    trackbar_value_lH = new_value_lH
def updateValue_lS(new_value_lS):
    global trackbar_value_lS
    trackbar_value_lS = new_value_lS
def updateValue_lV(new_value_lV):
    global trackbar_value_lV
    trackbar_value_lV = new_value_lV
def updateValue_hH(new_value_hH):
    global trackbar_value_hH
    trackbar_value_hH = new_value_hH
def updateValue_hS(new_value_hS):
    global trackbar_value_hS
    trackbar_value_hS = new_value_hS
def updateValue_hV(new_value_hV):
    global trackbar_value_hV
    trackbar_value_hV = new_value_hV
    
cv2.createTrackbar("lH", "Original", trackbar_value_lH, 180, updateValue_lH)
cv2.createTrackbar("lS", "Original", trackbar_value_lS, 255, updateValue_lS)
cv2.createTrackbar("lV", "Original", trackbar_value_lV, 255, updateValue_lV)
cv2.createTrackbar("hH", "Original", trackbar_value_hH, 180, updateValue_hH)
cv2.createTrackbar("hS", "Original", trackbar_value_hS, 255, updateValue_hS)
cv2.createTrackbar("hV", "Original", trackbar_value_hV, 255, updateValue_hV)


blobparams = cv2.SimpleBlobDetector_Params()
blobparams.filterByArea = True
blobparams.minArea = 2000
blobparams.maxArea = 5000
blobparams.filterByCircularity = False
blobparams.filterByInertia = False
blobparams.filterByConvexity = False
blobparams.minDistBetweenBlobs = 200
blobparams.filterByColor = True
blobparams.blobColor = 255
detector = cv2.SimpleBlobDetector_create(blobparams)


while True:
    ret, frame = cap.read()
    
    
    # You will need this later
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Colour detection limits
    
    lowerLimits = np.array([trackbar_value_lH, trackbar_value_lS, trackbar_value_lV])
    upperLimits = np.array([trackbar_value_hH, trackbar_value_hS, trackbar_value_hV])
    print(lowerLimits)
    print(upperLimits)
    thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
#   thresholded = cv2.bitwise_not(thresholded)
    outimage = cv2.bitwise_and(frame, frame, mask = thresholded)
    
    keypoints = detector.detect(thresholded)
    image = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    for keypoint in keypoints:
        x = int(keypoint.pt[0])
        y = int(keypoint.pt[1])
        cv2.putText(image, (str("x: ") + str(x)), (x + 50, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        cv2.putText(image, (str("y: ") + str(y)), (x + 50, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    cv2.imshow('Original', frame)
    cv2.imshow("image", image)
    cv2.imshow('Processed', thresholded)
    
    # Quit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        new = open('trackbar_defaults.txt', 'w')
        new.write((str(trackbar_value_lH) + '\n'))
        new.write((str(trackbar_value_lS) + '\n'))
        new.write((str(trackbar_value_lV) + '\n'))
        new.write((str(trackbar_value_hH) + '\n'))
        new.write((str(trackbar_value_hS) + '\n'))
        new.write((str(trackbar_value_hV) + '\n'))
        new.close()
        break
print('closing program')
cap.release()
cv2.destroyAllWindows()






    
