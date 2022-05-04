from gpiozero import AngularServo, Button
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
factory = PiGPIOFactory()
r = Servo(pin=18, min_pulse_width=0.0006, max_pulse_width=0.0023, pin_factory=factory )
for i in range(-90, 91):
    print(i)
    r.angle = i
    sleep(1)