import easygopigo3 as go
import time
myRobot = go.EasyGoPiGo3()
myRobot.drive_cm(30, blocking=True)
myRobot.spin_right()
time.sleep(0.5)
myRobot.drive_cm(30, blocking=True)
myRobot.spin_right()
time.sleep(0.5)
myRobot.drive_cm(30, blocking=True)
myRobot.spin_right()
time.sleep(0.5)
myRobot.drive_cm(30, blocking=True)

