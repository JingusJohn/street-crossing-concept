from gpiozero import AngularServo, Button
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
factory = PiGPIOFactory()
r = AngularServo(pin=16, min_pulse_width=0.0006, max_pulse_width=0.0023, pin_factory=factory )
r.angle = -52
sleep(5)
r.angle = 56
""" for i in range(-90, 91):
    print(i)
    r.angle = i
    sleep(1) """