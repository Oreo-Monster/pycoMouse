import storage


#This script tests the timing of a while loop on the raspberry pi pico
import time

log = open("whileTest.log", "a")

i = 0

while i < 10000:
    i += 1
    log.write(f"{time.monotonic_ns()}\n")

log.close()