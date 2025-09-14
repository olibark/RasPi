from machine import Pin, PWM
import time

led = Pin("LED", Pin.OUT)
buzz = PWM(Pin(15))
buzz.freq(600)  # Set buzzer tone frequency

def beep(duration):
    led.on()
    buzz.duty_u16(30000)
    time.sleep(duration)
    buzz.duty_u16(0)
    led.off()
    time.sleep(0.2)  # Gap between beeps


characters = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

long = 0.1
short = 0.025



string = "Hello oliver".upper()

morse = []

for i in range(len(string)):
    if string[i] in characters:
        morse.append(characters[string[i]])
        
morseCode = ' '.join(morse)
print("Morse Code:", morseCode)

for i in range(len(morseCode)):
    if morseCode[i] == '.':
        beep(short)
    elif morseCode[i] == '-':
        beep(long)
    elif morseCode[i] == ' ':
        time.sleep(long)