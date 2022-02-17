#The vars() function returns the __dict__ attribute of the given object.

class sample:
    a=1
    b=2
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1 = sample("John",31)

print(vars(p1))
#Note that class attributes are not included
