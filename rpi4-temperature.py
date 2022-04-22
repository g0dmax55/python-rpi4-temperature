#!/bin/python3

from gpiozero import CPUTemperature
import time

try:
        while True:
                cpu = CPUTemperature()
                cpu1 = cpu.temperature
                time.sleep(1)
                temp = print(f"\nRaspberry Pi 4 Temperature Is {cpu1}")

except KeyboardInterrupt:
        print("")
