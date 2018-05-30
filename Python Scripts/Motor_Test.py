import pigpio
from time import time,sleep

ena = 11
in1 = 9
in2 = 10
enb = 26
in3 = 19
in4 = 13

pi = pigpio.pi()

pi.set_mode(ena,pigpio.OUTPUT)
pi.set_mode(in1,pigpio.OUTPUT)
pi.set_mode(in2,pigpio.OUTPUT)
pi.set_mode(enb,pigpio.OUTPUT)
pi.set_mode(in3,pigpio.OUTPUT)
pi.set_mode(in4,pigpio.OUTPUT)


def forwards():
    pi.set_PWM_dutycycle(ena, 70) 
    pi.write(in1, 1)
    pi.write(in2, 0)
    pi.set_PWM_dutycycle(enb, 70)
    pi.write(in3, 1)
    pi.write(in4, 0)
    print("forward")


def backwards():
    pi.set_PWM_dutycycle(ena, 70)
    pi.write(in1, 0)
    pi.write(in2, 1)
    pi.set_PWM_dutycycle(enb, 70)
    pi.write(in3, 0)
    pi.write(in4, 1)
    print("backward")


def right():
    pi.set_PWM_dutycycle(ena, 70)
    pi.write(in1, 0)
    pi.write(in2, 0)
    pi.set_PWM_dutycycle(enb, 70)
    pi.write(in3, 1)
    pi.write(in4, 0)
    print("right")


def left():
    pi.set_PWM_dutycycle(ena, 70)
    pi.write(in1, 1)
    pi.write(in2, 0)
    pi.set_PWM_dutycycle(enb, 70)
    pi.write(in3, 0)
    pi.write(in4, 0)
    print("left")


def stop():
    pi.write(ena, 0)
    pi.write(in1, 0)
    pi.write(in2, 0)
    pi.write(enb, 0)
    pi.write(in3, 0)
    pi.write(in4, 0)
    print("nothing")


forwards()
sleep(3)
backwards()
sleep(3)
left()
sleep(3)
right()
sleep(3)
stop()

pigpio.cleanup()



