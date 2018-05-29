# Line following Rover

## Introduction to Today's Workshop

<b> Objective </b>: Create a robot rover to follow a fixed path using Raspberry Pi.<br/>

The rover starts from its initial point; while going through the line map (insulated black line), the detection sensors on the rover continuously check for any changes while moving along the map. If the rover goes off course, the detection sensors accumulates this data and creates an appropriate response, thereby regulating its current path. This is further explained in the figure below. <br/>

![line following basics](https://user-images.githubusercontent.com/32713072/40655737-5f3d1274-6353-11e8-9379-5211975df971.png)

A standard Line following rover needs a suitable foundation. Below is a circuit diagram, that shows the components used to reinforce the foundation criteria. 

![linefollow_bb](https://user-images.githubusercontent.com/32713072/40655684-2c1f8bb0-6353-11e8-8e25-8f2c7b0e86ce.jpg)

## Architecture overview

To accomplish this design, the following components have been taken under consideration:<br/>

### Raspberry PI
The use of the PI in this design is fairly simple, we need a device/component that is able to execute certain functions and deploy them in response to a certain criteria. A Raspberry Pi is simply a mini computer which is capable of doing everything a standard computer could do(but with lower computational power) such as: 
- browsing the internet 
- playing high-definition video 
- making spreadsheets
- word-processing 
- playing games
Furthermore, any standard harware components could be connected to the Raspberry PI via GPIO (General Purpose Input/Output) pins and programming the components, to attain certain control and manipulate responses based on these controls. 
The programming platform most commonly used with the Raspberry PI is python. Python is fairly simple to use and required little to limited progaramming knowledge to execute. <br/>

![raspberry pi 3](https://user-images.githubusercontent.com/32713072/40658019-df8ba8da-635a-11e8-8b11-0c2b4ca191c9.jpg)

### Motor Driver (L298N)
The main function of a motor driver is to drive the motor depending on how it is configured with the PI. So instead of random, sporadic movements the motors can be "controlled" to achieve an ideal movement pattern. <br/>

![l298n](https://user-images.githubusercontent.com/32713072/40658018-df5fe056-635a-11e8-8f83-dd6c852ec62e.jpg)


### Infra Red (IR) sensor
A basic feature of the IR sensor is to detect obstacles for short ranges, by sending pulses of IR rays and checking if the obstacle is close by.<br/>
For the line following rover to follow a certain path, it needs a component that could help navigate when the rover goes astray. This is why IR sensor would be the best component for the job. It is also possible to block IR rays by using a material that could absorb these rays thereby simulating an obstacl, hence we use an insulated black tape to obstruct the IR ray.<br/>

![ir_sensor_principles](https://user-images.githubusercontent.com/32713072/40658017-df396138-635a-11e8-8a0f-01f6c1f0f927.png)

*For our workshop we will be using the GPIO pins on the PI board itself to control certain aspects; such as moving the rover back and front, or left and right, or even stopping it. These motor movements will work in conjunction with the IR sensors, to follow the principles of the Line following mechanism.*

## Installing the Libraries
To enable the functionalities of all the different functions we will be using on python. Certain libraries need to be installed to enable us to use these "functionalities" for the further use.

### pigpio
pigpio is a library for the Raspberry which allows control of the General Purpose Input Outputs (GPIO).  pigpio works on all versions of the Pi. The reason why were are using this library, compared to the standard RPi.GPIO library is because we need a certaiin amount of control with the speed of the motor, which is achieved if pigpio library is used. To install this library onto your pi. Open uo your terminal and type: <br/>
```wget abyz.co.uk/rpi/pigpio/pigpio.zip``` <br/>
```unzip pigpio.zip```<br/>
```cd PIGPIO```<br/>
```make```<br/>
```sudo make install```<br/>

*For more information about the library follow this link*: **http://abyz.me.uk/rpi/pigpio/** 

### Setting up the program to run on terminal, after boot
A simple way to see how you can setup to run python file on Raspberry Pi startup (using the terminal).

- Save the python file on home/pi
- On the terminal, navigate to  /home/pi
- now open a hidden file  .bashrc  ( type "sudo nano .bashrc" on terminal and press enter)
- At the end of the file type "python" followed by your file name (eg: python3 speechtotext)
- If you want the terminal to revert back to its normal format, either comment out the command on the .bashrc file or remove it (you can access the bash file in /home/pi).

