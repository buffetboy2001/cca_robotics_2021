'''
Code from: https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
'''
#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to LOW, then HIGH
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(1)
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    print(f'StartTime:{StartTime}')
    StopTime = time.time()
    print(f'StopTime:{StopTime}')
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        pass
    StartTime = time.time()
 
    # save time of arrival
    print('looking for low while high')
    while GPIO.input(GPIO_ECHO) == 1:
        pass
    StopTime = time.time()
    print('echo went low and exited')
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()