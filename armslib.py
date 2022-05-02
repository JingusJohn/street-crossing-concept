# this library has everything necessary to instantiate and operate arms in
#  the main .py file
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory


factory = PiGPIOFactory()

# Servo class inherits AngularServo
class Servo(AngularServo):
    def __init__(self, pin: int, zero: int, ninety: int):
        AngularServo.__init__(self, pin=pin, min_pulse_width=0.0006, max_pulse_width=0.0023, pin_factory=factory)
        self.zero = zero
        self.ninety = ninety
    
    # a method that sets the angle of the servo motor to 0 degrees
    def to_zero(self):
        self.angle = self.zero
        
    # a method that sets the angle of the servo motor to 90 degrees
    def to_ninety(self):
        self.angle = self.ninety
        
    # getters for zero and ninety
    #  there's no need for getters
    @property
    def zero(self):
        return self._zero

    @property
    def ninety(self):
        return self._ninety
    
class Arm:
    def __init__(self, servo: Servo):
        self.servo = servo
        if self.servo.angle == self.zero:
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
        
class System:
    def __init__(self, arm1: Arm, arm2: Arm, timer):
        self.arms = [arm1, arm2]
        self.timer = timer
    
    # begins process
    def run(self):
        # check for pedestrians crossing and then let arms down
        # set timer for arms that will be reset each time someone attempts
        #  to cross the crosswalk
        pass
    
    # method that does any cleanup
    def stop(self):
        pass