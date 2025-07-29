import network
import socket
from machine import Pin
import time

ssid = 'BTHub6-Q7CN'       # Replace with your Wi-Fi SSID
password = 'wg4Cm9ra6CR9'   # Replace with your Wi-Fi password

led = Pin("LED", Pin.OUT)

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)
    print("Waiting for connection...")

print("Connected!")
ip = wlan.ifconfig()[0]
print("IP address:", ip)

# Simple web server
def web_page():
    led_state = "ON" if led.value() else "OFF"
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Pico W LED Control</title>
</head>
<body>
    <h1>Pico W LED is {led_state}</h1>
    <form action="/on" method="get"><button type="submit">Turn ON</button></form>
    <form action="/off" method="get"><button type="submit">Turn OFF</button></form>
</body>
</html>"""
    return html

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('Listening on', addr)

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024).decode()
    print("Request:", request)
    if '/on' in request:
        led.value(1)
    elif '/off' in request:
        led.value(0)
    response = web_page()
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()