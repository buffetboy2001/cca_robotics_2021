# Vehicle Control

**Module Goal**: learn to make Robby go left & right.

Let's learn how to turn `Robby` left and right.

## Stop & Turn

When you have a tank drive system like `Robby`, the tracks provide both the drive motion of the vehicle and also the steering control. How does steering work? Because it can make the two tracks turn opposite directions from each other. 

`Robby` can do the same thing!

In the python language we're using, we have some commands that will help us do this:
* `stop()` will make the wheels stop spinning;
* `sleep()` will make the current motion continue for some amount of time;
* `left()` will make `Robby` turn left;
* `right()` will make `Robby` turn right.

Time to try it out. In `vscode`, create a new file and add this:

```python
#!/bin/python3

# our team's left turn module
from gpiozero import Robot
import time

# Students: you may need to modify the left/right numbers
#           based on your wiring choices!
robby = Robot(left=(7, 8), right=(9, 10))

robby.left()
time.sleep(1.0)
robby.stop()
```

Make sure you save it: `turn_left.py`.

Then run it. In the terminal ![](./pics/terminal_icon_small.jpg):

* If you need to, change directories by typing `cd cca_robotics` and then **Enter**
* `python3 turn_left.py` and then **Enter**

`Robby` should have turned left by some amount. Maybe not much, maybe a lot. Discuss what happened.

**Challenge**: what can you do to make `Robby` turns a precise 90-degrees? Make it happen!

## Turn Right

To turn right, just change one line of code. I bet you can guess which one :grin:

Change `robby.left()` to `robby.right()`!

## Turning While Going Forward

Now, the code you've written so far makes `Robby` stop before turning. But, that's not super practical. Let's make `Robby` turn while driving forward.

Modify the code above to this:

```python
robby.forward(curve_right=1)
```

Or, you can use `curve_left`. But, you can't use them both at the same time :grin:

**Challenge**: what can you do to make `Robby` turns in a circle (left or right)? Make it happen!

---

**Module Complete**
