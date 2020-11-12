import cv2
import numpy as np


trackbar_value_lR = 0
trackbar_value_lG = 0
trackbar_value_lB = 0
trackbar_value_hR = 255
trackbar_value_hG = 255
trackbar_value_hB = 255

cap = cv2.VideoCapture(0)
cv2.namedWindow('Original')
kernel_size = 0

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
    
cv2.createTrackbar('kernel size', 'Original', kernel_size, 25, update_kernel_size)
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
    crop = frame[205:285]
   
    Median_blur = cv2.medianBlur(crop, 11)
    
    lowerLimits = np.array([trackbar_value_lR, trackbar_value_lG, trackbar_value_lB])
    upperLimits = np.array([trackbar_value_hR, trackbar_value_hG, trackbar_value_hB])
    thresholded = cv2.inRange(Median_blur, lowerLimits, upperLimits)
    
    keypoints = detector.detect(thresholded)
    image = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    cv2.imshow('Original', image)
    cv2.imshow('Original', crop)
    cv2.imshow('Thresholded', thresholded)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()