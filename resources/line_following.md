# Follow the Black Line

**Module Goal**: write Python code to use the line sensors and follow the line!

*Acknowledgement*: the python snippet in this module is copied directly from the [official Raspberry Pi tutorial](https://projects.raspberrypi.org/en/projects/rpi-python-line-following). 

## Python Code

Open a new file: **follow_line.py** (Mr. Bowman may have created this file file for you)

```python
#!/usr/bin/env python3
from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robby = Robot(left=(7, 8), right=(9, 10))
left_sensor = LineSensor(17)
right_sensor = LineSensor(27)

left_sensor.when_line = robby.left
left_sensor.when_no_line = robby.forward

right_sensor.when_line = robby.right
right_sensor.when_no_line = robby.forward

# pause()
sleep(10)
```

## Try It Out

Place your robot over top of the black line such that both line sensors show a blue light. Run the code!

This is a basic line-following algorithm. It won't be pretty! But, it should work.

**Challenge**: Discuss your ideas for making a better algorithm.

---

**Module Complete**