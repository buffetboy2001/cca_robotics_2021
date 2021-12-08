# Wiring and Using the TCS3200 Color Sensor

_Reference_: https://www.electronicshub.org/raspberry-pi-color-sensor-tutorial/

## Wiring

Quick wiring reference for connecting to a Raspberry Pi:

| --- | Physical Pin | GPIO |
| --- | --- | --- |
| VCC | 1 or 2 | --- |
| GND | GND | GND |
| S0 | same as VCC | same as VCC |
| S1 | same as VCC | same as VCC |
| S2 | --- | 23 |
| S3 | --- | 24 |
| OUT | --- | 25 |
| LED | VCC | VCC |

Use a breadboard to help connect the wires that are combined.

## Python Code

The TCS3200 does not come with "automatic" color output. You have to record the sensor values and learn how to interpret them.

Get some object of known color. Get a paper and pencil. Using the script below, record the values the code reports for each object.

Use this code:
> https://gist.github.com/elktros/e6135be8fba490c99f775ab58753f5dd#file-raspberry_pi_tcs3200_raw_rgb-py


Build a table like this with paper & pencil:

| Object Color | Reported Red Value | Reported Blue Value | Reported Green Value |
| --- | --- | --- | --- |
| red | - | - | - |
| blue | - | - | - |
| green | - | - | - |

Then, use the values in your table to update the code below. Once you've done that, you'll be able to start interpreting the sensor output and actually report the sensed color using the name of the color!

Use this code:
> https://gist.github.com/elktros/ec80707a22d9ab93a08cab5edfb5abba#file-raspberry_pi_tcs3200_color_detector-py

---

Module Complete