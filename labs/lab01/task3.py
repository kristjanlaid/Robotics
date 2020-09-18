import easygopigo3 as go
import time
myRobot = go.EasyGoPiGo3()
myRobot.drive_cm(36, blocking=True)
myRobot.turn_degrees(100,blocking=True)
myRobot.drive_cm(35, blocking=True)
myRobot.turn_degrees(-140,blocking=True)
myRobot.orbit(-75, radius_cm=55, blocking=True)
