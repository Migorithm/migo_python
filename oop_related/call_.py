#__call__ is what enables calling instance as if it's a function object

class Stuff(object):
    def __init__(self,x,y,range):
        super(Stuff,self).__init__()
        self.x = x
        self.y = y
        self.range=range

    def __call__(self,x,y):
        self.x = x
        self.y =y 
        print("__call__ with (%d, %d)" % (self.x,self.y))

s= Stuff(1,2,3)
print(s.x)

print(s(7,8))