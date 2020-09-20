import easygopigo3 as go
import time
myRobot = go.EasyGoPiGo3()

def move_forward_seconds(t):
    myRobot.forward()
    time.sleep(t)

def move_backward_seconds(t):
    myRobot.backward()
    time.sleep(t)

myRobot.set_speed(600)
move_forward_seconds(1)
move_backward_seconds(1)
move_forward_seconds(1)
move_backward_seconds(1)
move_forward_seconds(1)
move_backward_seconds(1)
move_forward_seconds(1)
move_backward_seconds(1)
move_forward_seconds(1)
move_backward_seconds(1)
myRobot.stop()
