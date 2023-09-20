#import socket
from relay_board import RelayModule
from motor_driver import L298NMotorDriver
from time import sleep

#define variables with gpio board pins
channel_pins = [29, 31] #power relay board pins

ena_1=33 # wheel 1 pwm enable
in1_1=38 # wheel 1 pin
in2_1=40 # wheel 1 pin

ena_2=35 # wheel 2 pwm enable
in1_2=15 # wheel 2 pin
in2_2=37 # wheel 2 pin

ena_3=12 # wheel 3 pwm enable
in1_3=16 # wheel 3 pin
in2_3=18 # wheel 3 pin

ena_4=32 # wheel 4 pwm enable
in1_4=22 # wheel 4 pin
in2_4=36 # wheel 4 pin

#object initialization
motor_1=L298NMotorDriver(ena_1, in1_1, in2_1)
motor_2=L298NMotorDriver(ena_2, in1_2, in2_2)
motor_3=L298NMotorDriver(ena_3, in1_3, in2_3)
motor_4=L298NMotorDriver(ena_4, in1_4, in2_4)

relay_module = RelayModule(channel_pins)
relay_module.activate_channel(1)
sleep(1)
relay_module.deactivate_channel(1)
while True:
        for dc in range(0, 101, 50):
                motor_1.forward(dc)
                motor_2.forward(dc)
                motor_3.forward(dc)
                motor_4.forward(dc)
                sleep(0.1)
        for dc in range(100, -1, -50):
                motor_1.forward(dc)
                motor_2.forward(dc)
                motor_3.forward(dc)
                motor_4.forward(dc)
                sleep(0.1)
