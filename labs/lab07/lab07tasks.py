#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import easygopigo3 as go
import numpy as np
import time

# Global variable for determining GoPiGo speed.
gospeed = 200

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
    
    my_robot.set_speed(gospeed)
    return


# TASK 1
def get_line_location(frame):
    # This function should use a single frame from the camera to determine line location.
    # It should return the location of the line in the frame.
    # Feel free to define and use any global variables you may need.
    # YOUR CODE HERE
    img = cap.read(cv2.IMREAD_GRAYSCALE)
    horizontal = np.nonzero(img)
    return np.mean(horizontal)

# TASK 2
def bang_bang(linelocation):
    # This function should use the line location to implement a simple bang-bang controller.
    # YOUR CODE HERE

    return


# TASK 3
def bang_bang_improved(linelocation):
    # This function should use the line location to implement an improved version of the bang-bang controller.
    # YOUR CODE HERE

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
        cv2.imshow('Original', frame)
        
        # Task 1: uncomment the following line and implement get_line_location function.
        linelocation = get_line_location(frame)

        # Task 2: uncomment the following line and implement bang_bang function.
        # bang_bang(linelocation)

        # Task 3: uncomment the following line and implement bang_bang_improved function.
        # bang_bang_improved(linelocation)

        # Task 4: uncomment the following line and implement proportional_controller function.
        # proportional_controller(linelocation)

        # Task 5: uncomment the following line and implement pid_controller function.
        # pid_controller(linelocation)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()
    my_robot.stop()

cap.release()
cv2.destroyAllWindows()
my_robot.stop()
