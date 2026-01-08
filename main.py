radio.set_group(17)

message = ""
last_time = input.running_time()
LETTER_THRESHOLD = 1000


def send_dot():
    radio.send_string(".")
    music.play_tone(1200, 200)
    basic.show_string(".")
    basic.clear_screen()


def send_dash():
    radio.send_string("-")
    music.play_tone(1200, 400)
    basic.show_string("-")
    basic.clear_screen()


def on_button_a():
    send_dot()

input.on_button_pressed(Button.A, on_button_a)


def on_button_b():
    send_dash()

input.on_button_pressed(Button.B, on_button_b)


def on_received(received):
    global message, last_time
    message += received
    last_time = input.running_time()

radio.on_received_string(on_received)


def forever():
    global message, last_time
    if input.running_time() - last_time > LETTER_THRESHOLD and len(message) > 0:
        message += " "
        last_time = input.running_time()

basic.forever(forever)


def on_logo_pressed():
    global message
    basic.show_string(message)
    message = ""

input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
