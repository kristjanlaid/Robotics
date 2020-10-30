#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

trackbar_value = 32

def updateValue(new_value):
    global trackbar_value
    trackbar_value = new_value
    
cv2.namedWindow("Window")
cv2.namedWindow("Original")

cv2.createTrackbar("Trackbar", "Window", trackbar_value, 96, updateValue)

img = cv2.imread('sample01.tiff')
img_greyscale = cv2.imread('sample01.tiff', 0)

ret, thresh = cv2.threshold(img_greyscale, trackbar_value, 255, cv2.THRESH_BINARY)

blobparams = cv2.SimpleBlobDetector_Params()
blobparams.filterByArea = True
blobparams.minArea = 2000
blobparams.maxArea = 10000
blobparams.filterByCircularity = False
blobparams.minDistBetweenBlobs = 50
detector = cv2.SimpleBlobDetector_create(blobparams)

keypoints = detector.detect(thresh)

while True:
    ret, thresh = cv2.threshold(img_greyscale, trackbar_value, 255, cv2.THRESH_BINARY)
    keypoints = detector.detect(thresh)
    image = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    for keypoint in keypoints:
        x = int(keypoint.pt[0])
        y = int(keypoint.pt[1])
        cv2.putText(image, (str("x: ") + str(x)), (x + 50, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(image, (str("y: ") + str(y)), (x + 50, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(thresh, str(trackbar_value), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)   
    cv2.imshow('Window', thresh)
    cv2.imshow('Window', image)
    cv2.imshow("Original", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
    
cv2.destroyAllWindows()


