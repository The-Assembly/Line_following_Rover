# importing the pigpio  
import pigpio

# time library used to extract the sleep function in order to use delays
from time import time,sleep

#defining variables that holds a corresponding GPIO pinout 
ena = 11 #Enable A
in1 = 9 #Input 1
in2 = 10 #Input 2
enb = 26 #Enable B
in3 = 19 #Input 3
in4 = 13 #Input 4
irs1 = 4  #Infrared Sensor 1
irs2 = 17 #Infrared Sensor 2

# pigpio.pi class gives access to a specified Pi's GPIO
pi = pigpio.pi()

#Setting GPIO mode to input, to access read mode 
pi.set_mode(irs1, pigpio.INPUT)
pi.set_mode(irs2, pigpio.INPUT)

#Setting GPIO mode to output, to access write mode 
pi.set_mode(ena,pigpio.OUTPUT)
pi.set_mode(in1,pigpio.OUTPUT)
pi.set_mode(in2,pigpio.OUTPUT)
pi.set_mode(enb,pigpio.OUTPUT)
pi.set_mode(in3,pigpio.OUTPUT)
pi.set_mode(in4,pigpio.OUTPUT)

def forwards(): 
    #set_PWM_dutycycle(gpio, dutycycle)
    #dutycycle:= 0-range (range defaults to 255)
    #The duty cycle corresponds to speed you want to set up 
    pi.set_PWM_dutycycle(ena, 50) 
    pi.set_PWM_dutycycle(enb, 50)
    #Sets the GPIO level (1-> True, 0-> False)
    pi.write(in1, 1)
    pi.write(in2, 0)
    pi.write(in3, 1)
    pi.write(in4, 0)
    print("forward")


def backwards():
    pi.set_PWM_dutycycle(ena, 50)
    pi.set_PWM_dutycycle(enb, 50)
    pi.write(in1, 0)
    pi.write(in2, 1)
    pi.write(in3, 0)
    pi.write(in4, 1)
    print("backward")


def right():
    pi.write(ena, 0)
    pi.set_PWM_dutycycle(enb, 50)
    pi.write(in1, 0)
    pi.write(in2, 0)
    pi.write(in3, 1)
    pi.write(in4, 0)
    print("right")


def left():
    pi.set_PWM_dutycycle(ena, 50)
    pi.write(enb, 0)
    pi.write(in1, 1)
    pi.write(in2, 0) 
    pi.write(in3, 0)
    pi.write(in4, 0)
    print("left")


def stop():
    pi.write(ena, 0)
    pi.write(enb, 0)
    pi.write(in1, 0)
    pi.write(in2, 0)
    pi.write(in3, 0)
    pi.write(in4, 0)
    print("nothing")

while True:
    #move forward
    if(pi.read(irs1)==False and pi.read(irs2)==False): 
        forwards()

    #turn right
    elif(pi.read(irs1)==True and pi.read(irs2)==False): 
        right()

    #LEFT
    elif(pi.read(irs1)==False and pi.read(irs2)==True): 
        left()
    #stop
    elif(pi.read(irs1)==True and pi.read(irs2)==True): 
        stop()




