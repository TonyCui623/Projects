from motor_driver import L298NMotorDriver
import RPi.GPIO as GPIO
import time

class MecanumWheelDriver:
    def __init__(self, front_left_pins, front_right_pins, rear_left_pins, rear_rig>
        self.front_left = L298NMotorDriver(*front_left_pins)
        self.front_right = L298NMotorDriver(*front_right_pins)
        self.rear_left = L298NMotorDriver(*rear_left_pins)
        self.rear_right = L298NMotorDriver(*rear_right_pins)

    def move(self, vx, vy, vz):
        fl_speed = vy - vx + vz
        fr_speed = vy + vx - vz
        rl_speed = vy + vx + vz
        rr_speed = vy - vx - vz

        self.front_left.forward(fl_speed)
        self.front_right.forward(fr_speed)
        self.rear_left.forward(rl_speed)
        self.rear_right.forward(rr_speed)

    def move_forward(self, speed):
        self.front_left.forward(speed)
        self.front_right.forward(speed)
        self.rear_left.forward(speed)
        self.rear_right.forward(speed)

    def move_backward(self, speed):
        self.front_left.backward(speed)
        self.front_right.backward(speed)
        self.rear_left.backward(speed)
        self.rear_right.backward(speed)

    def move_left(self, speed):
        self.front_left.backward(speed)
        self.front_right.forward(speed)
        self.rear_left.forward(speed)
        self.rear_right.backward(speed)

    def move_right(self, speed):
        self.front_left.forward(speed)
        self.front_right.backward(speed)
        self.rear_left.backward(speed)
        self.rear_right.forward(speed)

    def move_45c(self, speed):
        self.front_left.forward(speed)
        self.front_right.stop()
        self.rear_left.stop()
        self.rear_right.forward(speed)

    def move_135c(self, speed):
        self.front_left.stop()
        self.front_right.forward(speed)
        self.rear_left.forward(speed)
        self.rear_right.stop()

    def move_225c(self, speed):
        self.front_left.backward(speed)
        self.front_right.stop()
        self.rear_left.stop()
        self.rear_right.backward(speed)

    def move_315c(self, speed):
        self.front_left.stop()
        self.front_right.backward(speed)
        self.rear_left.backward(speed)
        self.rear_right.stop()

    def move_turn_left(self, speed):
        self.front_left.backward(speed)
        self.front_right.forward(speed)
        self.rear_left.backward(speed)
        self.rear_right.forward(speed)
    
    def move_turn_right(self, speed):
        self.front_left.forward(speed)
        self.front_right.backward(speed)
        self.rear_left.forward(speed)
        self.rear_right.backward(speed)

    def stop(self):
        self.front_left.stop()
        self.front_right.stop()
        self.rear_left.stop()
        self.rear_right.stop()

    def cleanup(self):
        self.front_left.cleanup()
        self.front_right.cleanup()
        self.rear_left.cleanup()
        self.rear_right.cleanup()

#class L298NMotorDriver:
    # ... (same L298NMotorDriver class code as before)
if __name__ == "__main__":
    front_left_pins = (12, 16, 18)    # ENA, IN1, IN2 pins for front left motor
    front_right_pins = (22, 23, 24)   # ENA, IN1, IN2 pins for front right motor
    rear_left_pins = (32, 33, 35)     # ENA, IN1, IN2 pins for rear left motor
    rear_right_pins = (36, 37, 38)    # ENA, IN1, IN2 pins for rear right motor

    mecanum_wheels = MecanumWheelDriver(front_left_pins, front_right_pins, rear_le>

    try:
        while True:
            vx = float(input("Enter x velocity: "))
            vy = float(input("Enter y velocity: "))
            vz = float(input("Enter z velocity: "))
            
            mecanum_wheels.move(vx, vy, vz)

    except KeyboardInterrupt:
        mecanum_wheels.stop()
        mecanum_wheels.cleanup()
        print("Exiting.")
