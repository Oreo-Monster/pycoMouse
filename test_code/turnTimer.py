import time
import math
import board
import pwmio
import rotaryio
import adafruit_bno055
import busio
import digitalio
import random


#setting up magnitometer and IMU through I2C
i2c = busio.I2C(scl=board.GP15, sda=board.GP14)
magSensor = adafruit_bno055.BNO055_I2C(i2c)

# setting up motor controls (left and right facing away)
right_back = pwmio.PWMOut(board.GP20, frequency=500, duty_cycle=0)
right_foward = pwmio.PWMOut(board.GP21, frequency=500, duty_cycle=0)
left_foward = pwmio.PWMOut(board.GP19, frequency=500, duty_cycle=0)
left_back = pwmio.PWMOut(board.GP18, frequency=500, duty_cycle=0)

# setting up enconder for right motor
encoderR = rotaryio.IncrementalEncoder(board.GP0, board.GP1)

# setting up enconder for left motor
encoderL = rotaryio.IncrementalEncoder(board.GP2, board.GP3)


#Number of trials
N=5

#Cols are inital time, final time, start angle, final angle
data = [[],[],[],[]]

for i in range(N):
    inital = magSensor.euler[0]
    target = (inital - random.randint(45, 180)) % 360
    data[2].append(inital)
    data[0].append( time.monotonic() )



    while magSensor.euler[0] > target or (magSensor.euler[0] <= inital and inital <  target):

        right_back.duty_cycle = 0
        right_foward.duty_cycle = 65535
        left_back.duty_cycle = 60535
        left_foward.duty_cycle = 0

    data[1].append(time.monotonic())
    data[3].append(magSensor.euler[0])

res = []
sum = 0

for i in range(N):
    time = data[1][i] - data[0][i]
    angle = data[3][i] - data[2][i]
    res.append([time/angle])
    sum += time/angle

avg = sum/N

log = file.open("turnTimer.log", "a")
file.write("Timing how long turns take, ")



