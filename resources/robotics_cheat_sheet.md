# Robotics Cheat Sheet

```python
# The numbers are for the pins used on the Raspberry Pi board.
# Make sure your numbers match your wiring!
robby = Robot(left=(4, 14), right=(17, 18))
```

| Command | Variant | What It Does |
| --- | ---| --- |
| **robby.forward()** | | Makes both motors turn at the same rate in the _forward_ direction at maximum speed. |
| | robby.forward(**speed=1**) | Makes both motors turn _forward_ at top speed. Use a smaller number to go slower. |
| | robby.forward(**curve_left=1**) | Makes the motors turn _left_. Use a smaller number to go forward and left. |
| | robby.forward(**curve_right=1**) | Makes the motors turn _right_. Use a smaller number to go forward and right. |
| **robby.backward()** | | Makes both motors turn at the same rate in the _backward_ direction at maximum speed. |
| | robby.backward(**speed=1**) | Makes both motors turn _backward_ at top speed. Use a smaller number to go slower. |
| | robby.backward(**curve_left=1**) | Makes the motors turn _left_. Use a smaller number to go backward and left. |
| | robby.backward(**curve_right=1**) | Makes the motors turn _right_. Use a smaller number to go backward and right. |
| **robby.reverse()** | | Reverse the robot's current motor directions. If the robot is currently running full speed forward, it will run full speed backward. If the robot is turning left at half-speed, it will turn right at half-speed. If the robot is currently stopped it will remain stopped. |
| **robby.stop()** | | Stop the robot's motion. |
| **robby.left()** | | Makes both motors turn so that the robot turns left at maximum speed. |
| | robby.left(**speed=1**) | Use a smaller number go left more slowly. |
| **robby.right()** | | Makes both motors turn so that the robot turns right at maximum speed. |
| | robby.right(**speed=1**) | Use a smaller number go right more slowly. |

You can see the code itself [online here](https://github.com/gpiozero/gpiozero/blob/81f1d5d62564656cdc984e6b587bc046c579ae43/gpiozero/boards.py#L2083).