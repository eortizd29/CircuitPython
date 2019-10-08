import time
import board
from rgb import RGB   # import the RGB class from the rgb module

r1 = board.D10
g1 = board.D11
b1 = board.D12

r2 = board.D3
g2 = board.D4
b2 = board.D5

myRGB1 = RGB(r1, g1, b1)   # create a new RGB object, using pins 3, 4, and 5
myRGB2 = RGB(r2, g2, b2)   # create a new RGB object, using pins 8, 9, and 10

myRGB1.red()          # Glow red
myRGB2.green()        # Glow green
time.sleep(1)
myRGB1.blue()         # Glow blue
myRGB2.cyan()         # Glow... you get it...
time.sleep(1)
myRGB1.magenta()      # Did you know magenta isn't in the rainbow?
myRGB2.yellow()       # Like you learned in fi make... huh?
time.sleep(1)
myRGB1.rainbow("rate1")
myRGB2.rainbow("rate2")
time.sleep(1)
