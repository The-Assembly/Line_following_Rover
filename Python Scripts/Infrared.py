# importing the pigpio  
import pigpio                   

# time library used to extract the sleep function in order to use delays
from time import time,sleep     

#defining variables that holds a corresponding GPIO pinout 
irs1 = 4  #Infrared Sensor 1
irs2 = 17 #Infrared Sensor 2

# pigpio.pi class gives access to a specified Pi's GPIO
pi = pigpio.pi()    

#Setting GPIO mode to input, to access read mode 
pi.set_mode(irs1, pigpio.INPUT) 
pi.set_mode(irs2, pigpio.INPUT)


while True:
    print("IR Sensor 1: ")
    print(pi.read(irs1)) #Returns the GPIO level (1-> True, 0-> False)
    print("IR Sensor 2: ")
    print(pi.read(irs2))
    sleep(0.5) # a delay of 0.5 seconds before starting the next iteration
