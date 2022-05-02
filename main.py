#>-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~<#
# AUTHORS:          Jack Branch, John Lambert, Andrew Bellucci               #
# Description:      CSC-132 Final Pi Project, GuardDog                       #
#>-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~<#

# IMPORTS
from armslib import Arm, Servo
from threading import Thread
from time import sleep


if __name__ == "__main__":
    try:
        O = Arm(Servo(16, -49, 59))
        P = Arm(Servo(12, 83, -27))
    except:
        pass