"""
The built-in type() function, when passed one argument, returns the type of an object. 
For new-style classes, that is generally the same as the object’s __class__ attribute:
"""
type(3) # <class 'int'>
type(['foo', 'bar', 'baz'])  # <class 'list'>
class Foo:
    pass

type(Foo())  # <class '__main__.Foo'>

"""
You can also call type() with three arguments—type(<name>, <bases>, <dct>):
<name> specifies the class name. This becomes the __name__ attribute of the class.

<bases> specifies a tuple of the base classes from which the class inherits. 
This becomes the __bases__ attribute of the class.

<dct> specifies a namespace dictionary containing definitions for the class body. 
This becomes the __dict__ attribute of the class.

Calling type() in this manner creates a new instance of the type metaclass. 
In other words, it DYNAMICALLY creates a new class.
"""

Foo = type("foo",(),{})

x = Foo()
print(x) # <__main__.foo object at 0x000001A80F257C40>

Bar = type("Bar",(Foo,),dict(attr=100))

x = Bar()
print(x.attr) #100
print(x.__class__) #<class '__main__.Bar'>
print(x.__class__.__bases__) # (<class '__main__.foo'>,)


"""
This time, <bases> is again empty. 
Two objects are placed into the namespace dictionary via the <dct> argument. 
The first is an attribute named attr and 
the second a function named attr_val, which becomes a 'method' of the defined class:
"""

Migo = type("Migo",(),{
    "attr":100,
    "attr_val" : lambda x : x.attr
})

migo:Migo = Migo()
print(migo.attr)
print(migo.attr_val())


"""
Only very simple functions can be defined with lambda in Python. 
In the following example, a slightly more complex function is defined externally 
then assigned to attr_val in the namespace dictionary via the name f:
"""

def f(self,**kwargs):
    for k,v in kwargs.items():
        setattr(self,str(k),v)
    
Mago  = type(
    "Mago",
    (),
    {
        "attr": 100,
        "__init__" : f
    }
)

mago = Mago(a=1,b=3)

print(mago.a,mago.b,mago.attr)