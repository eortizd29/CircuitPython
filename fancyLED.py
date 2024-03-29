import board  # pylint: disable-msg=import-error
import time
import digitalio  # pylint: disable-msg=import-error
import random

class FancyLED:
    def __init__(self, pin1, pin2, pin3):
        self.pin1 = digitalio.DigitalInOut(pin1)
        self.pin1.direction = digitalio.Direction.OUTPUT
        self.pin2 = digitalio.DigitalInOut(pin2)
        self.pin2.direction = digitalio.Direction.OUTPUT
        self.pin3 = digitalio.DigitalInOut(pin3)
        self.pin3.direction = digitalio.Direction.OUTPUT

    def alternate(self):
        for i in range(0, 5):
            self.pin1.value = True
            self.pin2.value = False
            self.pin3.value = True
            time.sleep(.5)
            self.pin1.value = False
            self.pin2.value = True
            self.pin3.value = False
            time.sleep(.5)
        time.sleep(.5)
        self.pin2.value = False

    def blink(self):

        self.pin1.value = True
        self.pin2.value = True
        self.pin3.value = True
        time.sleep(1)
        self.pin1.value = False
        self.pin2.value = False
        self.pin3.value = False
        time.sleep(1)
        
    def chase(self):
        self.pin1.value = True
        self.pin2.value = False
        self.pin3.value = False
        time.sleep(.5)
        self.pin1.value = False
        self.pin2.value = True
        self.pin3.value = False
        time.sleep(.5)
        self.pin1.value = False
        self.pin2.value = False
        self.pin3.value = True
        time.sleep(.5)
        self.pin3.value = False

    def sparkle(self):
        for whatever in range(0, 50):  # I want it to randomly flash 50 different times
            print(whatever)
            print("loop, n=")
            n = random.randint(0, 3)   # It randomly chooses a number from 0-3 and then I tell it what to do for each of the numbers
            print (n)
            print("\n")
            if n == 0:
                self.pin1.value = True
                self.pin2.value = True
                self.pin3.value = True
            if n == 1:
                self.pin1.value = False
                self.pin2.value = False
                self.pin3.value = True
            if n == 2:
                self.pin1.value = True
                self.pin2.value = False
                self.pin3.value = False
            if n == 3:
                self.pin1.value = False
                self.pin2.value = True
                self.pin3.value = False
            time.sleep(.05)
            # If you don't turn them all off at the end of each command it gets really confusing.
            self.pin1.value = False
            self.pin2.value = False
            self.pin3.value = False