import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print("GPIO HIGH")
PIN = 8
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)

PIN = 7
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)

GPIO.setup(9, GPIO.OUT)
GPIO.output(9, GPIO.LOW)
GPIO.setup(10, GPIO.OUT)
GPIO.output(10, GPIO.LOW)

time.sleep(5)

GPIO.cleanup()

