from machine import Pin, PWM
import time

led = Pin("LED", Pin.OUT)

characters = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

long = 0.3
short = 0.1

string = "hello"
string = string.upper()

morse = []
for i in range(len(string)):
    if string[i] in characters:
        morse.append(characters[string[i]])
        
morseCode = ' '.join(morse)
print("Morse Code:", morseCode)

for i in range(len(morseCode)):
    if morseCode[i] == '.':
        led.on()
        time.sleep(short)
        led.off()
        time.sleep(short)
    elif morseCode[i] == '-':
        led.on()
        time.sleep(long)
        led.off()
        time.sleep(short)
    elif morseCode[i] == ' ':
        time.sleep(long)