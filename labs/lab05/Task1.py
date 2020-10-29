#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

trackbar_value = 32

def updateValue(new_value):
    global trackbar_value
    trackbar_value = new_value
    
cv2.namedWindow("Window")

cv2.createTrackbar("Trackbar", "Window", trackbar_value, 96, updateValue)

blobparams = cv2.SimpleBlobDetector_Params()

blobparams.filterByArea = False

blobparams.filterByColor = True
blobparams.blobColor = 0


detector = cv2.SimpleBlobDetector_create(blobparams)





#Working with image files stored in the same folder as .py file
#Load the image from the given location
img = cv2.imread('sample01.tiff')
#Load the image from the given location in greyscale
img_greyscale = cv2.imread('sample01.tiff', 0)

ret, thresh = cv2.threshold(img_greyscale, trackbar_value, 255, cv2.THRESH_BINARY)

keypoints = detector.detect(thresh)

#Thresholding the image (Refer to opencv.org for more details)


#Display the images
while True:
    keypoints = detector.detect(thresh)
    cv2.imshow('Window', thresh)
    cv2.putText(thresh, str(trackbar_value), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    ret, thresh = cv2.threshold(img_greyscale, trackbar_value, 255, cv2.THRESH_BINARY)
    image = cv2.drawKeypoints(thresh, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
    
cv2.destroyAllWindows()


