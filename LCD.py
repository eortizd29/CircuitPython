
import board
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

button_a = digitalio.DigitalInOut(board.D3)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP

value = 1
lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)

lcd.clear()
lcd.set_cursor_pos(0, 0)
lcd.print("Switch State:")

while True:
    if button_a.value:
        lcd.set_cursor_pos(1, 0)
        lcd.print("Presses:")

    else:
        lcd.set_cursor_pos(1, 0)
        lcd.print("Presses:")
        value = value + 1
        lcd.print(str(value))
lcd.set_cursor_mode(CursorMode.LINE)