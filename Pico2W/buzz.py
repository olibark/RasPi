from machine import Pin, PWM
import time

# Onboard LED
led = Pin("LED", Pin.OUT)

# Buzzer on GP15 (you can change this if needed)
buzzer = PWM(Pin(15))
buzzer.freq(1000)  # Set buzzer tone frequency

# Morse code dictionary
characters = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

# Timing (seconds)
long = 0.4      # Dash
short = 0.2     # Dot
gap = 0.2       # Gap between parts of a letter

# Text to translate
string = "hello dad miss you"
string = string.upper()

# Convert to Morse code
morse = []
for char in string:
    if char in characters:
        morse.append(characters[char])
    elif char == ' ':
        morse.append('')  # word space

morseCode = ' '.join(morse)
print("Morse Code:", morseCode)

# Beep function (LED + buzzer)
def beep(duration):
    led.on()
    buzzer.duty_u16(30000)  # Turn buzzer on
    time.sleep(duration)
    buzzer.duty_u16(0)      # Turn buzzer off
    led.off()
    time.sleep(gap)         # Space between parts

# Play Morse Code
for symbol in morseCode:
    if symbol == '.':
        beep(short)
    elif symbol == '-':
        beep(long)
    elif symbol == ' ':
        time.sleep(long)  # Space between letters
