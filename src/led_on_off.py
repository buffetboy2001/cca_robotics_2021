import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print("LED off")
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.LOW)

time.sleep(5)

print("LED on")
GPIO.output(2, GPIO.HIGH)

time.sleep(5)

GPIO.cleanup()

