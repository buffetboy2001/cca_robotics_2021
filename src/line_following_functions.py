'''
Working with line sensors
'''
from gpiozero import LineSensor
from time import sleep

robby = None

def left_sensor_detected_white():
    print("left sensor on white...")
    return

def right_sensor_detected_white():
    print("right sensor on white...")
    return

def left_sensor_detected_black():
    print("left sensor on black...")
    return

def right_sensor_detected_black():
    print("right sensor on black...")
    return

if __name__ == "__main__":
    '''
    Code starts here
    '''

    # Setup the line sensors
    left_sensor = LineSensor(21)
    right_sensor = LineSensor(14)

    # left sensor functions
    left_sensor.when_no_line = left_sensor_detected_black
    left_sensor.when_line = left_sensor_detected_white

    # right sensor functions
    right_sensor.when_no_line = right_sensor_detected_black
    right_sensor.when_line = right_sensor_detected_white

    sleep(20)

    print("all done")