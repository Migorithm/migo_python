from abc import ABC, abstractmethod
from enum import Enum,auto
from typing import Optional


# Concrete Creator (Factory)

# Product Interface
# Concrete product(this will inherit Product Interface)

class IProduct(ABC):
    """Abstract interface for product"""
    
    @staticmethod
    @abstractmethod
    def create_product():
        "An abstract interface method"


class ProductA(IProduct):
    
    def __init__(self):
        self.name = "ProductA"
    
    def create_product(self):
        return self


class ProductB(IProduct):
    
    def __init__(self):
        self.name = "ProductB"
    
    def create_product(self):
        return self

class ProductC(IProduct):
    
    def __init__(self):
        self.name = "ProductC"
    
    def create_product(self):
        return self

class ProductFactory(Enum):
    PRODUCTA= ProductA()
    PRODUCTB= ProductB()
    PRODCUTC= ProductC()
    
    # """Factory class"""
    # @staticmethod
    # def get_product(type) -> IProduct:
    #     if type == "a":
    #         return ProductA()
    #     if type == "b":
    #         return ProductB()
    #     if type == "c":
    #         return ProductC()
        
product = ProductFactory.PRODUCTA



#Coffee banding machine

class ICoffee(ABC):
    @staticmethod
    @abstractmethod
    def Composition():
        """Proportion of each ingredients"""
        

class Americano(ICoffee):
    water :int = 70
    espresso :int = 30
    
    def Composition(self):
        return {"Espresso":self.espresso,"Water":self.water}

class Cappuchino(ICoffee):
    espresso :int = 60
    milk :int = 40
    def Composition(self):
        return {"Espresso":self.espresso,"Milk":self.milk}

class Latte(ICoffee):
    espresso :int = 50
    milk :int = 50
    def Composition(self):
        return {"Espresso":self.espresso,"Milk":self.milk}

class BandingMachine:
    @staticmethod
    def get_coffee(type): 
        if type =="Americano":
            return Americano()
        if type =="Latte":
            return Latte()
        if type =="Cappuchino":
            return Cappuchino()

#client
cup_of_coffee= BandingMachine.get_coffee("Americano")

print(cup_of_coffee.Composition())
        
        