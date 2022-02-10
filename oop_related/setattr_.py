class Person:
    name = 'Adam'

p = Person()
print("Before modification:",p.name)

#setting name to "John"
setattr(p,"name","John")

print("After modification:" , p.name)


#Setting an attribute not present in Person
setattr(p,"age",23)
print("Age is:",p.age)


#setattr in use with class
class obj:
    def __init__(self,data):
        if isinstance(data,(tuple,list)):
            for order,element in enumerate(data,1):
                setattr(self,"elem"+str(order),element)
        else:
            setattr(self,"elem",data)

a=obj(["wew","qeww","savg"])
print(a.elem1,a.elem2,a.elem3)