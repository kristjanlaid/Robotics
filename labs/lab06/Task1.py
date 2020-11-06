import cv2
import numpy as np

cv2.namedWindow("Original")
img = cv2.imread('Task1.png')
trackbar_value_kernel = 0
trackbar_value_iterations = 0
trackbar_value_dkernel = 0
trackbar_value_diterations = 0

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
    global trackbar_value_dterations
    trackbar_value_diterations = new_value_diterations

cv2.createTrackbar('ekernel', 'Original', trackbar_value_kernel, 10, updateValue_kernel)
cv2.createTrackbar('iterations', 'Original', trackbar_value_iterations, 10, updateValue_iterations)
cv2.createTrackbar('dkernel', 'Original', trackbar_value_dkernel, 10, updateValue_dkernel)
cv2.createTrackbar('diterations', 'Original', trackbar_value_diterations, 10, updateValue_diterations)


while True:    
    kernel = np.ones((trackbar_value_kernel, trackbar_value_kernel))
    dkernel = np.ones((trackbar_value_dkernel, trackbar_value_dkernel))
    print(trackbar_value_dkernel)
    eroded = cv2.erode(img, kernel, iterations = trackbar_value_iterations)
    dilated = cv2.dilate(eroded, dkernel, iterations = trackbar_value_diterations)
    cv2.imshow('Original',dilated)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()