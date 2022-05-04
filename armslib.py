# this library has everything necessary to instantiate and operate arms in
#  the main .py file
from gpiozero import AngularServo, Button
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as gpio
from time import sleep


factory = PiGPIOFactory()

# Servo class inherits AngularServo
class Servo(AngularServo):
    def __init__(self, pin: int, zero: int, ninety: int):
        AngularServo.__init__(self, pin=pin, min_pulse_width=0.0006, max_pulse_width=0.0023, pin_factory=factory)
        self.zero = zero
        self.ninety = ninety
        self.middle = int((ninety + zero) / 2)
    
    # a method that sets the angle of the servo motor to 0 degrees
    def to_zero(self):
        self.to_middle()
        sleep(1)
        self.angle = self.zero
        
    # a method that sets the angle of the servo motor to 90 degrees
    def to_ninety(self):
        self.to_middle()
        sleep(1)
        self.angle = self.ninety
        
    def to_middle(self):
        self.angle = self.middle
        
    # getters for zero and ninety
    #  there's no need for getters
    @property
    def zero(self):
        return self._zero
    
    @zero.setter
    def zero(self, value):
        self._zero = value

    @property
    def ninety(self):
        return self._ninety
    
    @ninety.setter
    def ninety(self, value):
        self._ninety = value
    
    @property
    def middle(self):
        return self._middle
    
    @middle.setter
    def middle(self, value):
        self._middle = value
    
class Arm:
    def __init__(self, servo: Servo):
        self.servo = servo
        if self.servo.angle == self.servo.zero:
            self.is_up = True
        else:
            self.is_up = False
    
    def up(self):
        self.servo.to_zero()
        self.is_up = True
    
    def down(self):
        self.servo.to_ninety()
        self.is_up = False
        
    def status(self) -> str:
        if self.is_up:
            return "up"
        else:
            return "down"
        
def checkpress():
    if gpio.input(18) == gpio.HIGH:
        return True
    elif gpio.input(20) == gpio.HIGH:
        return True
    else:
        return False
        
class System:
    def __init__(self, arm1: Arm, arm2: Arm, pad1: int, pad2: int, timer):
        self.arms = [arm1, arm2]
        self.timer = timer
        self.pad1 = pad1
        self.pad2 = pad2
        self.crossing = False
        self.just_crossed = False
    
    # begins process
    def run(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pad1, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.setup(self.pad2, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        # check for pedestrians crossing and then let arms down
        # set timer for arms that will be reset each time someone attempts
        #  to cross the crosswalk
        #runtime loop
        while True:
            print("made it to while loop")
            # check for peds
            if checkpress():
                print("pressed")
                timer = self.timer
                for arm in self.arms:
                    arm.down()
                while timer != 0:
                    if checkpress():
                        timer = self.timer
                    timer =- 1
                    sleep(1)
                self.just_crossed = True
            else:
                print("not pressed")
                
            if (not self.crossing) and self.just_crossed:
                self.just_crossed = False
                for arm in self.arms:
                    arm.up()

    
    # method that does any cleanup
    def stop(self):
        for arm in self.arms:
            arm.up()
        gpio.cleanup()