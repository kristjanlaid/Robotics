import cv2
import numpy as np
import easygopigo3 as go
import time
import os.path
from os import path

myRobot = go.EasyGoPiGo3()
myRobot.set_speed(30)


trackbar_value_lH = 0
trackbar_value_lS = 0
trackbar_value_lV = 0
trackbar_value_hH = 125
trackbar_value_hS = 125
trackbar_value_hV = 125
width = 640
height = 25

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
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cv2.namedWindow('Original')
kernel_size = 0

def update_kernel_size(new_kernel_value):
    global kernel_size
    kernel_size = new_kernel_value
    
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
blobparams.minArea = 500
blobparams.maxArea = 8000
blobparams.filterByCircularity = False
blobparams.filterByInertia = False
blobparams.filterByConvexity = False
blobparams.minDistBetweenBlobs = 50
blobparams.filterByColor = False
blobparams.blobColor = 255
detector = cv2.SimpleBlobDetector_create(blobparams)

finding_state = 'finding keypoints'
driving_state_left = 'driving from the left'
driving_state_right = 'driving from the right'
localising_state = 'localising'
finish_state = 'Between the pillars'
current_state = 'finding keypoints'

        

while True:
    ret, frame = cap.read()
    crop = frame[230:255]
   
    Gaussian_blur = cv2.GaussianBlur(crop, (5, 5), 0)
    HSV = cv2.cvtColor(Gaussian_blur, cv2.COLOR_BGR2HSV)
    lowerLimits = np.array([trackbar_value_lH, trackbar_value_lS, trackbar_value_lV])
    upperLimits = np.array([trackbar_value_hH, trackbar_value_hS, trackbar_value_hV])
    thresholded = cv2.inRange(HSV, lowerLimits, upperLimits)
    thresholded = cv2.bitwise_not(thresholded)
    thresholded = cv2.rectangle(thresholded, (0, 0), (width-1, height -1), (255, 255, 255), 2)
    
    keypoints = detector.detect(thresholded)
    for keypoint in keypoints:
        x = int(keypoint.pt[0])
        y = int(keypoint.pt[1])
        cv2.putText(crop, (str("x: ") + str(x)), (x + 50, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    if len(keypoints) == 2:
        if keypoints[0].pt[0] > keypoints[1].pt[0]:
            right_pillar = keypoints[0].pt[0]
            left_pillar = keypoints[1].pt[0]
            left_pillar_size = keypoints[1].size
            right_pillar_size = keypoints[0].size
            midpoint = (left_pillar + right_pillar) / 2
            
        else:
            left_pillar = keypoints[0].pt[0]
            right_pillar = keypoints[1].pt[0]
            left_pillar_size = keypoints[0].size
            right_pillar_size = keypoints[1].size
            midpoint = (left_pillar + right_pillar) / 2
        print('right pillar size', right_pillar_size)
        print('left pillar size', left_pillar_size)
        print(midpoint)
    image = cv2.drawKeypoints(Gaussian_blur, keypoints, np.array([]), (0,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    cv2.imshow('Original', image)
    cv2.imshow('Thresholded', thresholded)
    
    if current_state == "finding keypoints":
        myRobot.spin_right()
        if len(keypoints) == 2:
            if midpoint >= 310 and midpoint <= 330:
                myRobot.stop()
                print(midpoint)
                current_state = "localising"
            print("midpoint", midpoint)
                           
    elif current_state == "localising":
        if left_pillar_size - right_pillar_size >= 1.5:
            print('we are on the left side')
            current_state = 'driving from the left'
            myRobot.stop()
        elif right_pillar_size - left_pillar_size >= 1.5:
            print('We are on the right side')
            current_state = 'driving from the right'
            myRobot.stop()
        
        else:
            current_state = "Driving toward pillars"
            
        
    elif current_state == "driving from the left":
        myRobot.turn_degrees(60, blocking=True)
        myRobot.set_speed(50)
        myRobot.drive_cm(10)
        myRobot.turn_degrees(-60, blocking=True)
        current_state = "finding keypoints"
        
    elif current_state == "driving from the right":
        myRobot.turn_degrees(-60, blocking=True)
        myRobot.set_speed(50)
        myRobot.drive_cm(10)
        myRobot.turn_degrees(60, blocking=True)
        current_state = "finding keypoints"
        
    elif current_state == 'Driving toward pillars':
        print(midpoint)
        myRobot.set_speed(15)
        if midpoint >= 340:   
            myRobot.spin_right()
        elif midpoint <= 300:
            myRobot.spin_left()
        else:
            print("forward")
            myRobot.set_speed(50)
            myRobot.forward()
            
        if right_pillar_size >= 60 or left_pillar_size >= 60 :        
            current_state = "lokaliseerin uuesti veel"
        elif left_pillar_size - right_pillar_size >= 5 or right_pillar_size - left_pillar_size >= 5:
            current_state = "localising"
    
    elif current_state == "lokaliseerin uuesti veel":
        if len(keypoints) == 2:
            if midpoint >= 310 and midpoint <= 330:
                myRobot.stop()
                print(midpoint)
                current_state = "Between the pillars"
            else:
                myRobot.set_speed(10)
                if midpoint >= 335:   
                    myRobot.spin_right()
                elif midpoint <= 305:
                    myRobot.spin_left()
    
    elif current_state == "Between the pillars":
        myRobot.set_speed(100)
        myRobot.drive_cm(30)
    
    print(current_state)
    
    
    
        
        
    

    


    
    
    
        
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

cap.release()
cv2.destroyAllWindows()
myRobot.stop()
