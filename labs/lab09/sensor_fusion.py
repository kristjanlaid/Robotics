#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from velocity import Velocity

####################################
# Lab09: code to continuously edit #
####################################
TASK = 0 # Update this value in the beginning of each task!


# Pre-defined dictionaries
# Dictionary for holding positions
positions = {'current_marker': -1, 'current_us': -1, 'current_enc': -1, 'current_cam': -1,
             'current_moving_avg_us': -1, 'current_complementary': -1, 'current_kalman': -1}

# A Velocity class object for holding and updating velocities
velocities = Velocity({'us': 0, 'enc': 0, 'cam': 0,
                       'moving_avg_us': 0, 'complementary': 0, 'kalman': 0})


############################################
# Task 2: Implement moving average filter  #
############################################
def moving_average(pos):
    # Fill in the function.
    return 0


############################################
# Task 3: Implement complementary filter   #
############################################
def complementary(us_pos, enc_pos):
    # Fill in the function.
    return 0


# A class for performing operations with Gaussians
class Gaussian:
    def __init__(self, mu, sigma):
        # Initializes a Gaussian with given mu and sigma values
        self.mu = mu
        self.sigma = sigma

    #################################################
    # Task 4.2: Implement addition of two Gaussians #
    #################################################
    def __add__(self, other):
        # Fill in the function.
        return Gaussian(0, 0)

    #######################################################
    # Task 4.3: Implement multiplication of two Gaussians #
    #######################################################
    def __mul__(self, other):
        # Fill in the function
        return Gaussian(0, 0)


# A Kalman filter class
class Kalman:
    def __init__(self, initial_gaussian):
        # Initializes a Kalman filter with the initial state given as an input
        self.filtered_result = initial_gaussian

    ########################################
    # Task 4.2: Implement the predict step #
    ########################################
    def predict(self, measurement):
        # Fill in the function
        return

    #######################################
    # Task 4.3: Implement the update step #
    #######################################
    def update(self, measurement):
        # Fill in the function
        return


# Global variables for holding the encoder difference and camera Gaussians
# and the Kalman class object for use in other files
# DO NOT CHANGE THE NAMES OF THESE VARIABLES!
camera_gaussian = None
encoder_diff_gaussian = None
kalman_filter = Kalman(None)


####################################
# Lab09: code to continuously edit #
####################################
def on_ultrasonic_measurement(us_pos):
    # Write code here that will perform actions
    # whenever the robot calculates a new ultrasonic-based location estimate

    # Update the velocity calculated based on ultrasonic measurements
    velocities.update_velocity_for_sensor(us_pos, 'us')

    return

def on_encoder_measurement(enc_pos):
    # Write code here that will perform actions
    # whenever the robot calculates a new encoders-based location estimate

    # Update the velocity calculated based on encoder measurements
    velocities.update_velocity_for_sensor(enc_pos, 'enc')

    return

def on_camera_measurement(cam_pos):
    # Write code here that will perform actions
    # whenever the robot calculates a new camera-based location estimate

    # Update the velocity calculated based on ultrasonic measurements
    velocities.update_velocity_for_sensor(cam_pos, 'cam')

    return
