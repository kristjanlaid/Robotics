import cv2
import numpy as np

cv2.namedWindow("Original")
img = cv2.imread('Task2.png')
trackbar_value_kernel = 0
trackbar_value_iterations = 0
trackbar_value_dkernel = 0
trackbar_value_diterations = 0
trackbar_value_closing = 0

def updateValue_kernel(new_value_kernel):
    global trackbar_value_kernel
    trackbar_value_kernel = new_value_kernel
    
def updateValue_iterations(new_value_iterations):
    global trackbar_value_iterations
    trackbar_value_iterations = new_value_iterations
    
def updateValue_dkernel(new_value_dkernel):
    global trackbar_value_dkernel
    trackbar_value_dkernel = new_value_dkernel
    
def updateValue_diterations(new_value_diterations):
    global trackbar_value_diterations
    trackbar_value_diterations = new_value_diterations
    
def updateValue_closing(new_value_closing):
    global trackbar_value_closing
    trackbar_value_closing = new_value_closing

cv2.createTrackbar('kernel', 'Original', trackbar_value_kernel, 10, updateValue_kernel)
cv2.createTrackbar('iterations', 'Original', trackbar_value_iterations, 10, updateValue_iterations)
cv2.createTrackbar('dkernel', 'Original', trackbar_value_dkernel, 10, updateValue_dkernel)
cv2.createTrackbar('diterations', 'Original', trackbar_value_diterations, 10, updateValue_diterations)
cv2.createTrackbar('closing', 'Original', trackbar_value_closing, 10, updateValue_closing)

while True:    
    kernel = np.ones((trackbar_value_kernel, trackbar_value_kernel))
    dkernel = np.ones((trackbar_value_dkernel, trackbar_value_dkernel))
    dilated = cv2.dilate(img, dkernel, iterations = trackbar_value_diterations)
    eroded = cv2.erode(dilated, kernel, iterations = trackbar_value_iterations)
    closing = cv2.morphologyEx(eroded, cv2.MORPH_CLOSE, kernel, iterations = trackbar_value_closing)
    dilated = cv2.dilate(closing, dkernel, iterations = 3)    
    cv2.imshow('Original', dilated)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()
