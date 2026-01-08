radio.setGroup(17)
let message = ""
let last_time = input.runningTime()
let LETTER_THRESHOLD = 1000
function send_dot() {
    radio.sendString(".")
    music.playTone(1200, 200)
    basic.showString(".")
    basic.clearScreen()
}

function send_dash() {
    radio.sendString("-")
    music.playTone(1200, 400)
    basic.showString("-")
    basic.clearScreen()
}

input.onButtonPressed(Button.A, function on_button_a() {
    send_dot()
})
input.onButtonPressed(Button.B, function on_button_b() {
    send_dash()
})
radio.onReceivedString(function on_received(received: string) {
    
    message += received
    last_time = input.runningTime()
})
basic.forever(function forever() {
    
    if (input.runningTime() - last_time > LETTER_THRESHOLD && message.length > 0) {
        message += " "
        last_time = input.runningTime()
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    basic.showString(message)
    message = ""
})
