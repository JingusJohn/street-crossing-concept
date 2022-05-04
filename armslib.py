# this library has everything necessary to instantiate and operate arms in
#  the main .py file
from gpiozero import AngularServo, Button
from gpiozero.pins.pigpio import PiGPIOFactory


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
        
    def to_middle():
        self.angle = self.middle
        
    # getters for zero and ninety
    #  there's no need for getters
    @property
    def zero(self):
        return self._zero

    @property
    def ninety(self):
        return self._ninety
    
    @property
    def middle(self):
        return self._middle
    
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
    def __init__(self, arm1: Arm, arm2: Arm, pad1: int, pad2: int, timer):
        self.arms = [arm1, arm2]
        self.timer = timer
        self.pad1 = pad1
        self.pad2 = pad2
        self.crossing = False
    
    # begins process
    def run(self):
        btn1 = Button(self.pad1)
        btn2 = Button(self.pad2)
        # check for pedestrians crossing and then let arms down
        # set timer for arms that will be reset each time someone attempts
        #  to cross the crosswalk
        #runtime loop
        while True:
            # check for peds
            if btn1.is_held or btn2.is_held:
                timer = self.timer
                for arm in self.arms:
                    arm.down()
                while timer != 0:
                    if btn1.is_held or btn2.is_held:
                        timer = self.timer
                    timer =- 1
                    sleep(1)
                self.just_crossed = True
                
            if (not self.crossing) and self.just_crossed:
                self.just_crossed = False
                for arm in self.arms:
                    arm.up()

    
    # method that does any cleanup
    def stop(self):
        for arm in self.arms:
            arm.up()