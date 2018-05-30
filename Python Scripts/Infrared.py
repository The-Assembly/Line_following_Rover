# importing the pigpio library to enable all.... 
import pigpio                   

# time library used to extract the sleep function in order to use delays
from time import time,sleep     

irs1 = 4  #Infrared Sensor 1
irs2 = 17 #Infrared Sensor 2

pi = pigpio.pi()  # initialising the library 

#Setting IR sensor as input, thereby providing sensor data through the GPIO pins
pi.set_mode(irs1, pigpio.INPUT) 
pi.set_mode(irs2, pigpio.INPUT)

while True:
    print("IR Sensor 1: ")
    print(pi.read(irs1))
    print("IR Sensor 2: ")
    print(pi.read(irs2))
    sleep(0.5)
