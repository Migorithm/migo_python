#Product(what we want)
#Builder interface
#Builder
#Director(which has touching point with client)

from abc import ABC, abstractmethod

class IBuilder(ABC):
    "Builder interface"
    
    @staticmethod
    @abstractmethod
    def skill_a():
        "skill_a"
        
    @staticmethod
    @abstractmethod
    def skill_b():
        "skill_b"

    @staticmethod
    @abstractmethod
    def skill_c():
        "skill_c"
    
    @staticmethod
    @abstractmethod
    def get_product():
        "Return the final product"
        
class Builder(IBuilder):
    "Concrete(real) builder" 
    
    def __init__(self):
        self.product = Product() #coffee
    
    def skill_a(self):
        self.product.parts.append("skill_a")
        return self

    def skill_b(self):
        self.product.parts.append("skill_b")
        return self
        
    def skill_c(self):
        self.product.parts.append("skill_c")
        return self
        
    def get_product(self):
        return self.product
    
class Product:
    "Customizable, concrete Product"
    def __init__(self):
        self.parts = []
        
        
class DirectorA:
    "Touching point with client, representation."
    
    @staticmethod
    def construct():
        return Builder()\
            .skill_a()\
            .skill_b()\
            .get_product()
            
class DirectorB:
    "Touching point with client, representation."
    
    @staticmethod
    def construct():
        return Builder()\
            .skill_b()\
            .get_product()
            
class DirectorC:
    "Touching point with client, representation."
    
    @staticmethod
    def construct():
        return Builder()\
            .skill_b() \
            .skill_a() \
            .skill_c() \
            .skill_a()\
            .get_product()           
            
PRODUCT = DirectorA.construct()
PRODUCTC = DirectorC.construct()
print(PRODUCT.parts,PRODUCTC.parts)