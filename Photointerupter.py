import time


import board

from digitalio import DigitalInOut, Direction, Pull

photopin = DigitalInOut(board.D12)

photopin.direction = Direction.INPUT

photopin.pull = Pull.UP

interrupt = 0

inter_state = False

last_state = False

max = 4

start = time.time()

while True:

    inter_state = photopin.value

if inter_state and not last_state:

    interrupt = interrupt + 1

last_state = inter_state

time.sleep(.1)
remaining = max + start - time.time()

if remaining <= 0:

    print(" interrupt:", str(interrupt))

    max += 4

    interrupt = 0