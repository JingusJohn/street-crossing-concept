#>-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~<#
# AUTHORS:          Jack Branch, John Lambert, Andrew Bellucci               #
# Description:      CSC-132 Final Pi Project, GuardDog                       #
#>-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~<#

# IMPORTS
from armslib import Arm, Servo, System
from threading import Thread
from time import sleep
from tkinter import *
from calllib import *

class Gui(Frame):
    def __init__(self, master):
        self.status = "one"
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Testing")
        
        self.label = Label(text="GuardDog", fg="blue", font=('Helvetica', 18))
        self.label.pack(side=TOP)
        
        srvcs = ["Fire", "EMT", "Police"]
        color = ["red", "white", "blue"]
        cmmds = [test_call_fire, test_call_emt, test_call_pol]
        for i, srvc in enumerate(srvcs):
            Button(self.master, 
                text=f"Call {srvc}", 
                width=28,
                height=10,
                bg=color[i], 
                command=cmmds[i]).pack(side=LEFT)
        
        self.exit_button = Button(self.master, text="exit", command=self.master.destroy)
        self.exit_button.pack(side=BOTTOM)

def make_gui():
    window = Tk()
    window.attributes('-fullscreen', True)
    global g
    g = Gui(window)
    g.mainloop()


if __name__ == "__main__":
    try:
        O = Arm(Servo(16, -49, 59))
        P = Arm(Servo(12, 83, -27))
        thesys = System(O, P, 18, 20, 20)
        sys = Thread(target=thesys.run, daemon = True)
        gu = Thread(target=make_gui).start()        
        
    except:
        thesys.stop()
        sys.stop()
        gu.stop()