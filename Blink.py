import time
import board
import pulseio
led = pulseio.PWMOut(board.D9, frequency=5000, duty_cycle=0)

while True:
    for i in range(100):
        led.duty_cycle = int(i / 100 * 65535)
        time.sleep(0.01)
    for i in range(100, -1, -1):
        led.duty_cycle = int(i / 100 * 65535)
        time.sleep(0.01)
