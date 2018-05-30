import pigpio
from time import time,sleep

ena = 11
in1 = 9
in2 = 10
enb = 26
in3 = 19
in4 = 13
irs1 = 4
irs2 = 17

pi = pigpio.pi()

pi.set_mode(irs1, pigpio.INPUT)
pi.set_mode(irs2, pigpio.INPUT)
pi.set_mode(ena,pigpio.OUTPUT)
pi.set_mode(in1,pigpio.OUTPUT)
pi.set_mode(in2,pigpio.OUTPUT)
pi.set_mode(enb,pigpio.OUTPUT)
pi.set_mode(in3,pigpio.OUTPUT)
pi.set_mode(in4,pigpio.OUTPUT)

def forwards():
    pi.set_PWM_dutycycle(ena, 50)
    pi.write(in1, 1)
    pi.write(in2, 0)
    pi.set_PWM_dutycycle(enb, 50)
    pi.write(in3, 1)
    pi.write(in4, 0)
    print("forward")


def backwards():
    pi.set_PWM_dutycycle(ena, 50)
    pi.write(in1, 1)
    pi.write(in2, 0)
    pi.set_PWM_dutycycle(enb, 50)
    pi.write(in3, 1)
    pi.write(in4, 0)
    print("backward")


def right():
    pi.set_PWM_dutycycle(ena, 55)
    pi.write(in1, 1)
    pi.write(in2, 1)
    pi.set_PWM_dutycycle(enb, 55)
    pi.write(in3, 1)
    pi.write(in4, 0)
    print("right")


def left():
    pi.set_PWM_dutycycle(ena, 55)
    pi.write(in1, 1)
    pi.write(in2, 0)
    pi.set_PWM_dutycycle(enb, 55)
    pi.write(in3, 1)
    pi.write(in4, 1)
    print("left")


def stop():
    pi.write(ena, 0)
    pi.write(in1, 0)
    pi.write(in2, 0)
    pi.write(enb, 0)
    pi.write(in3, 0)
    pi.write(in4, 0)
    print("nothing")

while True:
    #both while move forward
    if(pi.read(irs1)==False and pi.read(irs2)==False): #both while move forward
        forwards()

    #turn right
    elif(pi.read(irs1)==True and pi.read(irs2)==False): #both while move forward
        right()

    #LEFT
    elif(pi.read(irs1)==False and pi.read(irs2)==True): #both while move forward
        left()

    elif(pi.read(irs1)==True and pi.read(irs2)==True): #both while move forward
        stop()

pigpio.cleanup()



