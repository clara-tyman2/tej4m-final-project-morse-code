# Wireless Morse code transmitter / receiver
# Press A for dot, press B for dash
# based on http://microbit-micropython.readthedocs.io/en/latest/tutorials/network.html

import microbit
from microbit import *
import music
import radio

radio.config(group=17)
radio.on()

# durations made a bit shorter than 250ms for a dot
# durations made a bit shorter than 500ms for a dash
DOT_DURATION = 230
DASH_DURATION = 470

# detect a new letter if incoming signal is greater than 1000ms.
LETTER_THRESHOLD = 1000

# Holds the translated Morse as characters.
message = ""
# The time from which the device has been waiting for the next event.
started_to_wait = running_time()


while True:
    # Work out how long the device has been waiting for a keypress.
    waiting = running_time() - started_to_wait
    signal = radio.receive()
    # Button presses for sending a message
    if button_a.is_pressed():
        display.show(".")
        radio.send(".")
        music.pitch(1200, duration=DOT_DURATION, wait=True)
        sleep(50)  # little sleep added to debounce
        display.clear()
    elif button_b.is_pressed():
        display.show("-")
        radio.send("-")
        music.pitch(1200, duration=DASH_DURATION, wait=True)
        sleep(50)  # little sleep added to debounce
        display.clear()
    # Listen out for dashes and dots over radio
    if signal:
        if signal == ".":
            pin0.write_digital(1)
            sleep(500)
            pin0.write_digital(0)
            message += "."
        elif signal == "-":
            pin0.write_digital(1)
            sleep(500)
            pin0.write_digital(0)
            message += "-"
        # We've received a signal, so reset waiting time
        started_to_wait = running_time()
    # Finally, if micro:bit was shaken while all the above was going on...
    if pin_logo.is_touched():
        # ... display the message on LEDs and serial console
        print(message)
        display.scroll(message)
        # then reset it to empty (ready for a new message).
        message = ""
