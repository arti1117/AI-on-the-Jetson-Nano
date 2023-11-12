from adafruit_servokit import ServoKit
import keyboard
import time


# myKit=ServoKit(channels=16)
# myKit.servo[0].angle=100
# time.sleep(5)

# while True:
#     try:
#         myKit.servo[0].angle=0
#         print('turn left')
#         time.sleep(5)
#         myKit.servo[0].angle=100
#         print('turn right')
#     except:
#         break

servo = ServoKit(channels=16)

servo.servo[0].angle=0

print("Start to control the servo motor")

while True:
    if keyboard.is_pressed("left"):
        servo.servo[0].angle=90
        print("Go to the left")
    elif keyboard.is_pressed("right"):
        servo.servo[0].angle=180
        print("Go to the right")
    elif keyboard.is_pressed("esc"):
        break;

print("End to read the ky")