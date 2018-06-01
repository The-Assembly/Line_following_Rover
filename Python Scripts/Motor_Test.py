# importing the pigpio  
import pigpio

# time library used to extract the sleep function in order to use delays
from time import time,sleep

#defining variables that holds a corresponding GPIO pinout 
ena = 17 #Enable A
in1 = 27 #Input 1
in2 = 22 #Input 2
in3 = 10 #Input 3
in4 = 9 #Input 4
enb = 11 #Enable B

# pigpio.pi class gives access to a specified Pi's GPIO
pi = pigpio.pi()

#Setting GPIO mode to output, to access write mode 
pi.set_mode(ena,pigpio.OUTPUT)
pi.set_mode(in1,pigpio.OUTPUT)
pi.set_mode(in2,pigpio.OUTPUT)
pi.set_mode(enb,pigpio.OUTPUT)
pi.set_mode(in3,pigpio.OUTPUT)
pi.set_mode(in4,pigpio.OUTPUT)

# defining functions to allow easy setup for certain motor functionalities 

def forwards(): 
    #set_PWM_dutycycle(gpio, dutycycle)
    #dutycycle:= 0-range (range defaults to 255)
    #The duty cycle corresponds to speed you want to set up 
    pi.set_PWM_dutycycle(ena, 70) 
    pi.set_PWM_dutycycle(enb, 70)
    #Sets the GPIO level (1-> True, 0-> False)
    pi.write(in1, 1)
    pi.write(in2, 0)
    pi.write(in3, 1)
    pi.write(in4, 0)
    print("forward")


def backwards():
    pi.set_PWM_dutycycle(ena, 70)
    pi.set_PWM_dutycycle(enb, 70)
    pi.write(in1, 0)
    pi.write(in2, 1)
    pi.write(in3, 0)
    pi.write(in4, 1)
    print("backward")


def right():
    pi.write(ena, 0)
    pi.set_PWM_dutycycle(enb, 70)
    pi.write(in1, 0)
    pi.write(in2, 0)
    pi.write(in3, 1)
    pi.write(in4, 0)
    print("right")


def left():
    pi.set_PWM_dutycycle(ena, 70)
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


#calling the functions, each new function responds after a period of 3 sec from the previous function 
forwards()
sleep(3)
backwards()
sleep(3)
left()
sleep(3)
right()
sleep(3)
stop()





