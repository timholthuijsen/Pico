import time
import board
import touchio
import digitalio

# Define GPIO pins
touch_pin = board.GP18
mosfet_pin = board.GP21  # This is where the gate of your MOSFET is connected

# Create a capacitive touch object
touch = touchio.TouchIn(touch_pin)

# Set up MOSFET control pin
mosfet = digitalio.DigitalInOut(mosfet_pin)
mosfet.direction = digitalio.Direction.OUTPUT
mosfet.value = False  # Start with MOSFET off

# Main loop
while True:
    if touch.value:
        print("Touched!")
        mosfet.value = False  # Turn MOSFET on when touched
    else:
        print("Not touched.")
        mosfet.value = True  # Turn MOSFET off when not touched
    time.sleep(0.1)  # Delay to avoid continuous checking
