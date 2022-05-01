from abc import ABC, abstractmethod
import copy

class IProtoType(ABC):
    @abstractmethod
    def clone():
        """The clone, deep or shallow, is up to how you
        want to implement the details in your concrete class"""
        
class ConcreteClass1(IProtoType):
    "Concrete class 1"    
    def __init__(self,i=0,s="",l:list=[],d:dict={}):
        self.i=i
        self.s=s
        self.l=l
        self.d=d
        
    def clone(self):
        """Shallow copy """
        return type(self)(
            self.i,
            self.s,
            self.l.copy(),
            self.d.copy()
        )
    
    def __str__(self):
        return f"{id(self)}\ti={self.i}\ts={self.s}\tl={self.l}\td={self.d}"


class ConcreteClass2(IProtoType):
    "Concrete class 2"    
    def __init__(self,i=0,s="",l:list=[],d:dict={}):
        self.i=i
        self.s=s
        self.l=l
        self.d=d
        
    def clone(self):
        """Shallow copy """
        return type(self)(   #Return a object
            self.i,
            self.s,
            copy.deepcopy(self.l),
            copy.deepcopy(self.d)
        )
    
    def __str__(self):
        return f"{id(self)}\ti={self.i}\ts={self.s}\tl={self.l}\td={self.d}"


if __name__ =="__main__":
    OBJECT1 = ConcreteClass1(1,"OBJECT1",[[1,2,3],2,3],{"a":1,"b":2,"c":3})
    print(OBJECT1)
    
    #COPY
    OBJECT2 = OBJECT1.clone()
    OBJECT2.s = "OBJECT2"
    OBJECT2.l[0][0] = 10
    print(OBJECT2) #Gets a new address 
    print(OBJECT1)
    
    
    
    
    OBJECT1 = ConcreteClass2(1,"OBJECT1",[[1,2,3],2,3],{"a":1,"b":2,"c":3})
    print(OBJECT1)
    
    OBJECT2 = OBJECT1.clone()
    OBJECT2.s = "OBJECT2"
    OBJECT2.l[0][0] = 10
    print(OBJECT2) #Gets a new address 
    print(OBJECT1)