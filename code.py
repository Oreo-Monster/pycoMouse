import time
import math
import board
import pwmio
import rotaryio
import adafruit_bno055
import busio
import digitalio

# setting up proximity sensors (left to right facing us, 1 to 5)
proximity1 = digitalio.DigitalInOut(board.GP6)
proximity1.direction = digitalio.Direction.INPUT
proximity1.pull = digitalio.Pull.DOWN

proximity2 = digitalio.DigitalInOut(board.GP7)
proximity2.direction = digitalio.Direction.INPUT
proximity2.pull = digitalio.Pull.DOWN

proximity3 = digitalio.DigitalInOut(board.GP8)
proximity3.direction = digitalio.Direction.INPUT
proximity3.pull = digitalio.Pull.DOWN

proximity4 = digitalio.DigitalInOut(board.GP9)
proximity4.direction = digitalio.Direction.INPUT
proximity4.pull = digitalio.Pull.DOWN

proximity5 = digitalio.DigitalInOut(board.GP10)
proximity5.direction = digitalio.Direction.INPUT
proximity5.pull = digitalio.Pull.DOWN

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

wheelDiameter = 6.6 #cm
wheelCirc = wheelDiameter * math.pi


'''
helper function to compare two angles, if they are the same within some leeway
returns True if so
'''
def compare_angle(angle1, angle2, leeway):

    if angle1 < angle2 + leeway/2 and angle1 > angle2 - leeway/2:
        return True
    return False



def go_forward(dist):
    ''' 
    moves micromouse forward by given distance
    @params dist: distance in cm to go forward
    @returns distance traveled, as mesured by encoders
    
    The mouse may not travel full distance if proximity3 is set off
     '''
    # Setting all values to zero
    encoderR.position = 0
    encoderL.position = 0
    right_back.duty_cycle = 0
    left_back.duty_cycle = 0
    left_foward.duty_cycle = 0
    right_foward.duty_cycle = 0

    encoderDist = (dist/wheelCirc)*360

    # Turn both wheeles until one makes a full rotation, and while nothing is in
    # front of the mouse
    while (encoderR.position < encoderDist or encoderL.position < encoderDist) and proximity3.value:
        #Both motors full blast
        right_foward.duty_cycle = 65535
        left_foward.duty_cycle = 65535
        # If the right is farther than the right within error of 10 degrees
        while encoderL.position > encoderR.position + 10 and proximity3.value:
            right_back.duty_cycle = 0
            right_foward.duty_cycle = 65535
            left_back.duty_cycle = 0
            left_foward.duty_cycle = 0

        # If the left is farther than the right within error of 10 degrees
        while encoderR.position > encoderL.position + 10 and proximity3.value:
            right_back.duty_cycle = 0
            right_foward.duty_cycle = 0
            left_back.duty_cycle = 0
            left_foward.duty_cycle = 65535


    # If there is something in front of mouse, make sure everything stoped
    # moving

    left_foward.duty_cycle = 0
    right_foward.duty_cycle = 0
    right_back.duty_cycle = 0
    left_back.duty_cycle = 0

    return (encoderL.position/360)*wheelCirc

def turn_left(turnAngle=90):
    ''' turns left 90 degrees '''

    global current_heading

    inital_angle = (magSensor.euler[0] + 180) % 360
    angle = (magSensor.euler[0] + 180) % 360

    while not compare_angle(angle, (inital_angle - turnAngle) % 360, 2):
        angle = (magSensor.euler[0] + 180) % 360
        right_back.duty_cycle = 0
        right_foward.duty_cycle = 65535
        left_back.duty_cycle = 60535
        left_foward.duty_cycle = 0

    right_back.duty_cycle = 0
    right_foward.duty_cycle = 0
    left_back.duty_cycle = 0
    left_foward.duty_cycle = 0

    current_heading = (current_heading - turnAngle) % 360

def turn_right(turnAngle=90):
    ''' turns left 90 degrees '''

    global current_heading

    inital_angle = (magSensor.euler[0] + 180) % 360
    angle = (magSensor.euler[0] + 180) % 360

    while not compare_angle(angle, (inital_angle + turnAngle) % 360, 2):
        angle = (magSensor.euler[0] + 180) % 360
        right_back.duty_cycle = 65535
        right_foward.duty_cycle = 0
        left_back.duty_cycle = 0
        left_foward.duty_cycle = 65535

    right_back.duty_cycle = 0
    right_foward.duty_cycle = 0
    left_back.duty_cycle = 0
    left_foward.duty_cycle = 0

    current_heading = (current_heading + turnAngle) % 360


current_heading = 0 #keeps track of turns, left turns are negative




