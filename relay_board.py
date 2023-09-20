import RPi.GPIO as GPIO
import time

class RelayModule:
    def __init__(self, channel_pins):
        self.channel_pins = channel_pins
        self.num_channels = len(channel_pins)
        self.setup_channels()

    def setup_channels(self):
        GPIO.setmode(GPIO.BOARD)
        for pin in self.channel_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def activate_channel(self, channel):
        if 1 <= channel <= self.num_channels:
            GPIO.output(self.channel_pins[channel - 1], GPIO.HIGH)
            print(f"Channel {channel} activated.")
        else:
            print("Invalid channel number.")

    def deactivate_channel(self, channel):
        if 1 <= channel <= self.num_channels:
            GPIO.output(self.channel_pins[channel - 1], GPIO.LOW)
            print(f"Channel {channel} deactivated.")
        else:
            print("Invalid channel number.")

    def cleanup(self):
        GPIO.cleanup()
        print("GPIO cleanup completed.")
if __name__ == "__main__":
    channel_pins = [11, 12, 13, 15]  # Example GPIO pins for the relay channels
    relay_module = RelayModule(channel_pins)

    try:
        while True:
            channel = int(input("Enter channel number (1-4): "))
            action = input("Enter action (on/off): ")

            if action.lower() == "on":
                relay_module.activate_channel(channel)
            elif action.lower() == "off":
                relay_module.deactivate_channel(channel)
            else:
                print("Invalid action. Please enter 'on' or 'off'.")

    except KeyboardInterrupt:
        relay_module.cleanup()
        print("Exiting.")
