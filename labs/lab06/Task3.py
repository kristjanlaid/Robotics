import cv2
import time
import numpy as np
from matplotlib import pyplot as plt
import os.path
from os import path

trackbar_value_lR = 0
trackbar_value_lG = 0
trackbar_value_lB = 0
trackbar_value_hR = 125
trackbar_value_hG = 125
trackbar_value_hB = 125

if path.exists('trackbar_defaults.txt'):
    values = open('trackbar_defaults.txt', 'r')
    trackbar_value_lR = int(values.readline())
    trackbar_value_lG = int(values.readline())
    trackbar_value_lB = int(values.readline())
    trackbar_value_hR = int(values.readline())
    trackbar_value_hG = int(values.readline())
    trackbar_value_hB = int(values.readline())
    values.close()

cap = cv2.VideoCapture(0)
old_time = 0
new_time = 0
kernel_size = 0
cv2.namedWindow("Original")


def update_kernel_size(new_kernel_value):
    global kernel_size
    kernel_size = new_kernel_value
    
def updateValue_lR(new_value_lR):
    global trackbar_value_lR
    trackbar_value_lR = new_value_lR
def updateValue_lG(new_value_lG):
    global trackbar_value_lG
    trackbar_value_lG = new_value_lG
def updateValue_lB(new_value_lB):
    global trackbar_value_lB
    trackbar_value_lB = new_value_lB
def updateValue_hR(new_value_hR):
    global trackbar_value_hR
    trackbar_value_hR = new_value_hR
def updateValue_hG(new_value_hG):
    global trackbar_value_hG
    trackbar_value_hG = new_value_hG
def updateValue_hB(new_value_hB):
    global trackbar_value_hB
    trackbar_value_hB = new_value_hB
    
cv2.createTrackbar('kernel size', 'Blurred', kernel_size, 20, update_kernel_size)
cv2.createTrackbar("lR", "Original", trackbar_value_lR, 255, updateValue_lR)
cv2.createTrackbar("lG", "Original", trackbar_value_lG, 255, updateValue_lG)
cv2.createTrackbar("lB", "Original", trackbar_value_lB, 255, updateValue_lB)
cv2.createTrackbar("hR", "Original", trackbar_value_hR, 255, updateValue_hR)
cv2.createTrackbar("hG", "Original", trackbar_value_hG, 255, updateValue_hG)
cv2.createTrackbar("hB", "Original", trackbar_value_hB, 255, updateValue_hB)

blobparams = cv2.SimpleBlobDetector_Params()
blobparams.filterByArea = True
blobparams.minArea = 1000
blobparams.maxArea = 5000
blobparams.filterByCircularity = False
blobparams.filterByInertia = True
blobparams.filterByConvexity = False
blobparams.minDistBetweenBlobs = 200
blobparams.filterByColor = True
blobparams.blobColor = 255
detector = cv2.SimpleBlobDetector_create(blobparams)

while True:
    ret, frame = cap.read()
    Gaussian_blur = cv2.GaussianBlur(frame,(21, 21), 0)
    Median_blur = cv2.medianBlur(frame, 25)
    
    new_time = time.time()
    Fps = 1 / (new_time - old_time)
    old_time = new_time
    Fps = int(Fps)
    Fps = str(Fps)
    
    lowerLimits = np.array([trackbar_value_lR, trackbar_value_lG, trackbar_value_lB])
    upperLimits = np.array([trackbar_value_hR, trackbar_value_hG, trackbar_value_hB])
    thresholded = cv2.inRange(Gaussian_blur, lowerLimits, upperLimits)
    thresh_median = cv2.inRange(Median_blur, lowerLimits, upperLimits)
    
    keypoints = detector.detect(thresholded)
    image = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
#     plt.subplot(121),plt.imshow(frame),plt.title('Original')
#     plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
#     plt.xticks([]), plt.yticks([])
#     plt.show()
    
    cv2.putText(Gaussian_blur, Fps, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(Median_blur, Fps, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, Fps, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Gaussian Blurred', thresholded)
    cv2.imshow('Median blurred', Gaussian_blur)
    cv2.imshow('Original', frame)
    cv2.imshow('Original', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        new = open('trackbar_defaults.txt', 'w')
        new.write((str(trackbar_value_lR) + '\n'))
        new.write((str(trackbar_value_lG) + '\n'))
        new.write((str(trackbar_value_lB) + '\n'))
        new.write((str(trackbar_value_hR) + '\n'))
        new.write((str(trackbar_value_hG) + '\n'))
        new.write((str(trackbar_value_hB) + '\n'))
        new.close()
        break

cap.release()
cv2.destroyAllWindows()













    

