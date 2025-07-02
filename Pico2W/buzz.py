from machine import Pin, PWM
import time

# Set up PWM on GPIO15 (Pin 20)
buzzer = PWM(Pin(15))
buzzer.duty_u16(0)  # Ensure buzzer is off initiall
buzzer.duty_u16(30000)  # Turn buzzer on at medium volume

# Frequency range (Hz)
min_freq = 500
max_freq = 2000
step = 10       # Frequency step size
delay = 0.01    # Delay between steps (smoother = smaller)

for freq in range(min_freq, max_freq, step):
    # Sweep up
    for freq in range(min_freq, max_freq, step):
        buzzer.freq(freq)
        time.sleep(delay)

    # Sweep down
    for freq in range(max_freq, min_freq, -step):
        buzzer.freq(freq)
        time.sleep(delay)
buzzer.duty_u16(0)  # Turn buzzer off