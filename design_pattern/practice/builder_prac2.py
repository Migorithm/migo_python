#Coffee
# Americano
# Caffe latte
# Caffe mocha
# Chocolate latte

from abc import ABC,abstractmethod
class IMachine(ABC):
    
    @staticmethod
    @abstractmethod
    def put_chocolate(self):
        "Give me chocolate!"
        
    @staticmethod
    @abstractmethod
    def put_esspresso():
        "Give me caffein!"
                

    @staticmethod
    @abstractmethod
    def put_water():
        "Give me water!"
        
    @staticmethod
    @abstractmethod
    def put_water():
        "Give me water!"
    
    @staticmethod
    @abstractmethod
    def put_bubble():
        "Give me bubble!"
        
    @staticmethod
    @abstractmethod
    def serve_drink():   
        "Serve drink"
    
        
        
class Machine(IMachine):

    def __init__(self):
        self.beverage = Beverage()

    def beverage_type(self,beverage_type:str):
        self.beverage.name = beverage_type
        return self
        
    def put_chocolate(self,choco:int):
        self.beverage.choco = choco
        return self
    
    def put_milk(self,milk:int):
        self.beverage.milk = milk
        return self    
        
    def put_esspresso(self,esspresso:int):
        self.beverage.esspresso = esspresso
        return self

    def put_water(self,water:int):
        self.beverage.water = water
        return self

    def put_bubble(self,bubble:int):
        self.beverage.bubble = bubble
        return self
        
    def serve_drink(self):   
        return self.beverage.__dict__
    
class Beverage:
    "The real product"
    def __init__(self,name="",choco:int=0,esspresso:int=0,water:int=0,bubble:int=0):
        self.name =name
        self.choce=choco
        self.esspresso = esspresso
        self.water = water 
        self.bubble=bubble
    
    

class Americano:

    @staticmethod
    def make():
        return Machine().beverage_type("American")\
                .put_water(70)\
                .put_esspresso(30)\
                .serve_drink()        
                       
class BubbleTea:
    @staticmethod
    def make():
        return Machine().beverage_type("BubbleTea")\
                .put_milk(40)\
                    .put_bubble(20)\
                    .put_esspresso(10)\
                    .put_chocolate(10)\
                    .serve_drink()

AME=Americano()
BUBBLE=BubbleTea()

print(AME.make())
print(BUBBLE.make())