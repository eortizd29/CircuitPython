import time
import board
import neopixel
import simpleio
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)
solarvalue = 0
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)
red = 0
blue = 0
green = 0
while True:

    try:
        solarvalue = sonar.distance
        print((solarvalue))
    except RuntimeError:
        print("Retrying!")
        pass
    if solarvalue < 5:
        dot.fill((255, 0, 0))
    if solarvalue > 35:
        dot.fill((0, 255, 0))

    if solarvalue <= 20 and solarvalue > 0:
        red = simpleio.map_range(solarvalue, 5, 20, 255, 0)
        blue = simpleio.map_range(solarvalue, 5, 20, 0, 255)
        green = simpleio.map_range(solarvalue, 5, 35, 0, 255)
    else:
        dot.fill((int(red), int(green), int(blue)))

        time.sleep(0.1)