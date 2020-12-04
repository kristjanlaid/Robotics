#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import easygopigo3 as go
import numpy as np
import time
import os.path
from os import path

# Global variable for determining GoPiGo speed.
gospeed = 200
myRobot = go.EasyGoPiGo3()

trackbar_value_lH = 0
trackbar_value_lS = 0
trackbar_value_lV = 0
trackbar_value_hH = 125
trackbar_value_hS = 125
trackbar_value_hV = 125

width = 1280
height = 60

if path.exists('trackbar_defaults.txt'):
    values = open('trackbar_defaults.txt', 'r')
    trackbar_value_lH = int(values.readline())
    trackbar_value_lS = int(values.readline())
    trackbar_value_lV = int(values.readline())
    trackbar_value_hH = int(values.readline())
    trackbar_value_hS = int(values.readline())
    trackbar_value_hV = int(values.readline())

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
cv2.namedWindow('Thresholded')    
cv2.createTrackbar("lH", "Thresholded", trackbar_value_lH, 180, updateValue_lH)
cv2.createTrackbar("lS", "Thresholded", trackbar_value_lS, 255, updateValue_lS)
cv2.createTrackbar("lV", "Thresholded", trackbar_value_lV, 255, updateValue_lV)
cv2.createTrackbar("hH", "Thresholded", trackbar_value_hH, 180, updateValue_hH)
cv2.createTrackbar("hS", "Thresholded", trackbar_value_hS, 255, updateValue_hS)
cv2.createTrackbar("hV", "Thresholded", trackbar_value_hV, 255, updateValue_hV)

# Global variable for video feed.
cap = None

# Global variable for robot object.
my_robot = go.EasyGoPiGo3()


def init():
    global cap, gospeed
    # This function should do everything required to initialize the robot.
    # Among other things it should open the camera and set GoPiGo speed.
    # Some of this has already been filled in.
    # You are welcome to add your own code if needed.

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    my_robot.set_speed(gospeed)
    return


# TASK 1
def get_line_location(thresholded):
    # This function should use a single frame from the camera to determine line location.
    # It should return the location of the line in the frame.
    # Feel free to define and use any global variables you may need.
    # YOUR CODE HERE
    arrays = np.nonzero(thresholded)
    return np.mean(arrays[1])


# TASK 2
def bang_bang(linelocation):
    # This function should use the line location to implement a simple bang-bang controller.
    # YOUR CODE HERE
    if linelocation < 640:
        myRobot.left()
    else:
        myRobot.right()
    return linelocation


# TASK 3
def bang_bang_improved(linelocation):
    # This function should use the line location to implement an improved version of the bang-bang controller.
    # YOUR CODE HERE
    if linelocation < 680 and linelocation > 600:
        myRobot.forward()
    elif linelocation < 600:
        myRobot.right()
    elif linelocation > 680:
        myRobot.left()
    return linelocation
    return


# TASK 4
def proportional_controller(linelocation):
    # This function should use the line location to implement a proportional controller.
    # Feel free to define and use any global variables you may need.
    # YOUR CODE HERE

    return


# TASK 5
def pid_controller(linelocation):
    # This function should use the line location to implement a PID controller.
    # Feel free to define and use any global variables you may need.
    # YOUR CODE HERE

    return


# Initialization
init()

try:
    while True:
        # We read information from the camera.
        ret, frame = cap.read()
        crop = frame[330:390]
        #cv2.imshow('Original', frame)
        HSV = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
        lowerLimits = np.array([trackbar_value_lH, trackbar_value_lS, trackbar_value_lV])
        upperLimits = np.array([trackbar_value_hH, trackbar_value_hS, trackbar_value_hV])
        thresholded = cv2.inRange(HSV, lowerLimits, upperLimits)
        cv2.imshow('Thresholded', thresholded)
        
        # Task 1: uncomment the following line and implement get_line_location function.
        linelocation = get_line_location(thresholded)
        print(linelocation)
        # Task 2: uncomment the following line and implement bang_bang function.
        bang_bang(linelocation)

        # Task 3: uncomment the following line and implement bang_bang_improved function.
        # bang_bang_improved(linelocation)

        # Task 4: uncomment the following line and implement proportional_controller function.
        # proportional_controller(linelocation)

        # Task 5: uncomment the following line and implement pid_controller function.
        # pid_controller(linelocation)
        
        
        
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

except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()
    my_robot.stop()

cap.release()
cv2.destroyAllWindows()
my_robot.stop()

