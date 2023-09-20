from gpiozero import LED
from time import sleep
from signal import pause
import RPi.GPIO as GPIO
from relay_board import RelayModule
from motor_driver import L298NMotorDriver
from motor_driver import L298MotorDriver
#relay_1=29 #gpio 5
#relay_2=31 #gpio 6

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(relay_1, GPIO.OUT)
#GPIO.output(relay_1, GPIO.LOW) 

#gled=LED(17)
#while True:
#       gled.blink()
#       pause()
channel_pins = [29, 31, 13]

in1_5=8
in2_5=10

motor_5=L298MotorDriver(in1_5, in2_5)

relay_module = RelayModule(channel_pins)
relay_module.activate_channel(1)
relay_module.activate_channel(2)
relay_module.activate_channel(3)
sleep(1)
#relay_module.deactivate_channel(1)
#relay_module.deactivate_channel(2)
relay_module.deactivate_channel(3)
#while True:
#       motor_5.forward()
#       sleep(3)
#       motor_5.forward()
#       sleep(3)
