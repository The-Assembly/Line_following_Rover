import pigpio
from time import time,sleep

irs1 = 4
irs2 = 17

pi = pigpio.pi()

pi.set_mode(irs1, pigpio.INPUT)
pi.set_mode(irs2, pigpio.INPUT)

while True:
    print("IR Sensor 1: ")
    print(pi.read(irs1))
    print("IR Sensor 2: ")
    print(pi.read(irs2))
