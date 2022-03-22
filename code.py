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

def turn_left(turnAngle=90, speedFactor=1.0, verbose=False, log=None):
    ''' turns left 90 degrees '''


    inital_angle, angle = magSensor.euler[0], magSensor.euler[0]
    target = (inital_angle - turnAngle) % 360

    if verbose:
        if log is not None:
            log.write("Turning Left\n")
            log.write("Time,Angle,Inital Angle,Target Angle\n")
        else:
            print("Time    Angle    Inital Angle    Target Angle\n")

    while angle > target or angle <= inital_angle:
        angle = (magSensor.euler[0]) % 360
        if verbose:
            if log is not None:
                log.write(f"{time.monotonic()}, {angle}, {inital_angle}, {target}\n")
            else:
                print("Turning left: " + str(time.monotonic()) + "    " + str(angle) + "    " + str(inital_angle) + "        " + str(target))
        
        right_back.duty_cycle = 0
        right_foward.duty_cycle = int(65535*speedFactor)
        left_back.duty_cycle = int(60535*speedFactor)
        left_foward.duty_cycle = 0
    
    #Turn off all motors
    right_back.duty_cycle = 0
    right_foward.duty_cycle = 0
    left_back.duty_cycle = 0
    left_foward.duty_cycle = 0


def turn_right(turnAngle=90, speedFactor=1.0, verbose=False, log=None):
    ''' turns left 90 degrees '''

    inital_angle, angle = magSensor.euler[0], magSensor.euler[0]
    target = (inital_angle + turnAngle) % 360

    if verbose:
        if log is not None:
            log.write("Turning Right\n")
            log.write("Time,Angle,Inital Angle,Target Angle\n")
        else:
            print("Time    Angle    Inital Angle    Target Angle\n")

    while angle < target or angle >= inital_angle:
        angle = (magSensor.euler[0]) % 360
        if verbose:
            if log is not None:
                log.write(f"{time.monotonic()}, {angle}, {inital_angle}, {target}\n")
            else:
                print("Turning left: " + str(time.monotonic()) + "    " + str(angle) + "    " + str(inital_angle) + "        " + str(target))
        
        right_back.duty_cycle = int(60535*speedFactor)
        right_foward.duty_cycle = 0
        left_back.duty_cycle = 0
        left_foward.duty_cycle = int(60535*speedFactor)
    
    #Turn off all motors
    right_back.duty_cycle = 0
    right_foward.duty_cycle = 0
    left_back.duty_cycle = 0
    left_foward.duty_cycle = 0

def turnTo(target, speedFactor = 1 , tolerance = 2, verbose = False, log = None):

    inital = magSensor.euler[0]

    calc = inital-target

    #Calculting the turn angle for left and right turns
    if calc < 0:
        #calc is a right turn
        right = abs(calc)
        left = 360 - right
    elif calc > 0:
        #calc is a left turn
        right = abs(calc)
        left = 360 - right
    else:
        #calc = 0, no turn needed
        return

    if right < left:
        #turn right
        turn_right(right, speedFactor, verbose, log)
    else:
        #turn left
        turn_left(left, speedFactor, verbose, log)
    
    #Recursive call at slower speed to get even closer to our angle
    if(not compare_angle(target, magSensor.euler[0]), tolerance):
        turnTo(target, speedFactor/2, tolerance, verbose, log)

    

def turn_test(speedFactor, angleTolerence):
    #We want to test turning left 90 degrees several times
    #to see repeatability
    #We also want to test at different speeds and alngler tolerences
    #For each turn, we want to time how long it takes
    #We also want to output the reading of the angle every update

    #16 Turns total

    #open log file
    log_file = open("turn_test.csv", "w")
    log_file.write("Turning Test Log File\n")


    for i in range(16):
        log_file.write("Turn " + str(i) + "\n")
        startTime = time.monotonic()
        turnTo(magSensor.euler[0]-90, speedFactor, angleTolerence, True, log_file)
        endTime = time.monotonic()
        log_file.write("Total Turn Time:," + str(endTime - startTime) + "\n")
        log_file.write("Current Heading:," + str(current_heading) + "\n")
        log_file.write("Current Angle:," + str(magSensor.euler[0]) + "\n")

        #Wait for a second before moving on
        time.sleep(1)

    log_file.close()

turn_test(1.0, 2)



