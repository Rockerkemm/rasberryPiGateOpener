from machine import Pin
import utime

relay1= Pin(6,Pin.OUT)
relay2= Pin(7,Pin.OUT)

while True:
    print("Relay1 On")
    relay1(1)
    utime.sleep(1)
    print("Relay1 Off")
    relay1(0)
    print()
    utime.sleep(2)
    print("Relay2 On")
    relay2(1)
    utime.sleep(1)
    print("Relay2 Off")
    relay2(0)
    utime.sleep(2)
    
    