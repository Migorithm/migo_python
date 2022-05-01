from abc import ABC, abstractmethod

class ICarMaker(ABC):
    
    @staticmethod
    @abstractmethod
    def make_seat():
        "make seat"

    @staticmethod
    @abstractmethod
    def make_engine():
        "make engine"
        
    @staticmethod
    @abstractmethod
    def make_turbo():
        "make turbo"
        
class CarMaker(ICarMaker):
    def __init__(self):
        self.product = Car()

    def make_seat(self):
        self.product.parts.append("seat")
        return self

    def make_engine(self):
        self.product.parts.append("engine")
        return self
    
    def make_turbo(self):
        self.product.parts.append("turbo")
        return self
    def get_car(self):
        return self.product


class Car:
    def __init__(self):
        self.parts=[]
        
    
        
class Director():
    @staticmethod
    def Tesla():
        return CarMaker()\
            .make_seat()\
            .make_engine()\
            .make_engine()\
            .get_car()
            
PRODUCT = Director.Tesla()
print(PRODUCT.parts)