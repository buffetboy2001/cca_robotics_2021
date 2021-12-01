#!/bin/bash/env python3

from gpiozero import Robot
import time

robby = Robot(left=(8,7), right=(9,10))
SPEED = 0.8
robby.forward(speed=SPEED)
time.sleep(5)
robby.stop()

time.sleep(1)

robby.backward(speed=SPEED)
time.sleep(5)
robby.stop()

time.sleep(1)

robby.left(speed=SPEED)
time.sleep(5)
robby.stop()

time.sleep(1)

robby.right(speed=SPEED)
time.sleep(5)
robby.stop()