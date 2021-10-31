# Basic Sensor Circuits

## Light Emitting Diode (LED)

_Reference_: https://projects.raspberrypi.org/en/projects/rpi-connect-led

You'll need:

* an LED;
* a 220 Ohm resistor;
* two male-male wires;
* a breadboard.

First, examine the LED. Find the positive wire by carefully reviewing the picture below.

![LED polarity](pics/LEDcloseup.png)

Now, organize your wiring such that the positive side of the LED connects to the **RED** wire. And add the resistor. Like below:

![breadboard final](pics/ground-missing.png)

Then find a GND output from the Raspberry Pi and connect a wire from that to the same row as the resistor.

![pinout](pics/rpi4_pinout.png)

One you complete the wiring connections, you should have a brightly lit LED!

![LED alight](pics/LED-alight.jpg)

### LED with a Switch

Quick Modification. The above circuit doesn't use the switch at all. What can you do to make the switch control the on-off behavior of the LED?

![with switch](pics/LED-with-switch.jpg)

### Control the LED with Python

Remove the red switch. Make sure the LED is on again, like above. Let's control the on-off state of the LED using python code.

On the Raspberry Pi, open Code and start a new file (`led_control.py` or something like that). 

Use some python code like this:

```python

```

## Obstacle Detection


## Line Detection


## Color Sensing

---

**Module Complete**
