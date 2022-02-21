from abc import ABC,abstractclassmethod

class Switchable(ABC):
    @abstractclassmethod
    def turn_on(self):
        pass

    @abstractclassmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")
    
    def turn_off(self):
        print("LightBulb: turned off...")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")
    
    def turn_off(self):
        print("Fan: turned off...")


class Switch:
    def __init__(self,b:Switchable):
        self.button= b
        self.on = False
    
    def press(self):
        if self.on:
            self.button.turn_off()
            self.on=False
        else:
            self.button.turn_on()
            self.on=True

s = Switch(LightBulb())

s.press()
s.press()
s.press()
s.press()
s.press()
s.press()

fan = Switch(Fan())

fan.press()
fan.press()
fan.press()
fan.press()