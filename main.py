import time
from machine import UART
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")
uart = UART(1, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1)

uart.write("abc")