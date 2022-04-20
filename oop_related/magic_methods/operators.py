

class Angle:
    def __repr__(self):
        return "<%r>" % self.angle
    
    def __init__(self,angle=None):
        if angle:
            self.angle = angle % 360
    
    def __add__(self,other):
        return Angle(self.angle + other.angle)
    def __sub__(self,other):
        return Angle(self.angle - other.angle)
    def __mul__(self,other):
        return Angle(self.angle * other.angle)
    def __truediv__(self,other):  #Floating-point division
        return Angle(self.angle / other.angle)
    def __mod__(self,other):
        return Angle(self.angle % other.angle)
    def __pow__(self,other):
        return Angle(self.angle ** other.angle)

    #bit-operation
    def __lshift__(self,other): # self << other
        return Angle(self.angle << other.angle)
    def __rshift__(self,other):
        return Angle(self.angle >> other.angle)
    
    def __and__(self,other): #not logical operation(in fact there is no logical operation) but "&" If you want to use it, you can manipulate like this
        return hasattr(self, "angle") and hasattr(other,"angle")
       
    def __xor__(self,other): 
        return Angle(self.angle ^ other.angle)
    def __or__(self,other):
        return Angle(self.angle | other.angle)
    
    # Comparison
    def __eq__(self,other):
        return self.angle == other.angle
    def __ne__(self,other): # Defining this is not necessary as != will automatically negate the output of __eq__ when __eq__ is defined.
        return self.angle != other.angle
    def __lt__(self,other):
        return self.angle < other.angle
    def __ge__(self,other):
        return self.angle >= other.angle
    
    
a= Angle(5)
b= Angle(-30)

print(a+b) 

c = Angle()
d = Angle(5)
print(c & d )

print("{!r}".format(a +b ))



# Shortcut : functools.total_ordering
## In essence, in your class you define both __eq__ and ONE of the comparison magic methods and then all missing rich comparison operators are supplied.

from functools import total_ordering

@total_ordering
class Angle:
    def __repr__(self):
        return "<%r>" % self.angle
    
    def __init__(self,angle=None):
        if angle:
            self.angle = angle % 360
    def __eq__(self,other):
        return self.angle == other.angle
    def __gt__(self,other):
        return self.angle > other.angle

a = Angle(5)
b = Angle(3)
print(a>b)
print(a<b)