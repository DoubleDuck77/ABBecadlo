import lib8mosfet
import time
class RH_Chamber:

    def __init__(self,port_fan_in = 5, port_fan_out = 6,
            port_hum  = 8, *args, **kwargs):

        self.t = 0
        self.state = "off1"
        self.automation = False
        self.port_fan_in = port_fan_in
        self.port_fan_out = port_fan_out
        self.port_hum = port_hum


    def change_state(self, port , state):
        lib8mosfet.set(0, port, state)

    def rh_in(self):
        self.state = "in"
        self.change_state(port = self.port_fan_in, state = 1)
        self.change_state(port = self.port_hum, state = 1)
        self.change_state(port = self.port_fan_out, state = 0)
        self.t = 0


    def rh_out(self):
        self.state = "out"
        self.change_state(port = self.port_fan_in, state = 1)
        self.change_state(port = self.port_hum, state = 0)
        self.change_state(port = self.port_fan_out, state = 1)
        self.t = 0

    def rh_off(self):
        if self.state == "in":
            self.state = "off1"
        else:
            self.state = "off2"
            
        self.change_state(port = self.port_fan_in, state = 1)
        self.change_state(port = self.port_hum, state = 0)
        self.change_state(port = self.port_fan_out, state = 0)
        self.t = 0

    def rh_automation_on(self):
        self.t = 0
        self.state = "in"
        self.automation = True
        self.rh_in()

    def rh_automation_off(self):
        self.t = 0
        self.automation = False
        self.rh_off()
rh  = RH_Chamber(8, 1, 7)
def move(t = 0.2):
    
    rh.rh_out()
    time.sleep(t)
    rh.rh_in()
