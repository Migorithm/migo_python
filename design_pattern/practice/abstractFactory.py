from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass

#FunitureFactory

class IFunitureFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_funiture():
        "Abstract method"


class FunitureFatory(IFunitureFactory):
    @staticmethod
    def get_funiture(type):
        #table, chair 
        try :
            if type in ["ts","tm","tl"]:
                return TableFactory.get_table(type[-1])
            if type in ["cs","cm","cl"]:
                return ChairFactory.get_chair(type[-1])
            raise Exception("No such line found in this Funiture shop.")
        except Exception as e:
            print(e)
        return None

class IChair(ABC):
    @staticmethod
    @abstractmethod
    def get_dimensions() -> dict:
        pass
    
@dataclass
class SmallChair(IChair):
    _height: int = 40
    _width: int = 40
    _depth: int = 40 
    def get_dimensions(self):
        return self.__dict__
    
@dataclass
class MediumChair(IChair):
    _height: int = 60
    _width: int = 60
    _depth: int = 60 
    def get_dimensions(self):
        return self.__dict__
    
@dataclass  
class LargeChair(IChair):
    _height: int = 80
    _width: int = 80
    _depth: int = 80 
    def get_dimensions(self):
        return self.__dict__

class ChairFactory:
    @staticmethod
    def get_chair(type):
        if type == "s":
            return SmallChair()
        if type == "m":
            return MediumChair()
        if type == "l":
            return LargeChair()



class ITable(ABC):
    @staticmethod
    @abstractmethod
    def get_dimensions() -> dict:
        pass
@dataclass
class SmallTable(ITable):
    _height: int = 40
    _width: int = 40
    _depth: int = 40 
    def get_dimensions(self):
        return self.__dict__
@dataclass
class MediumTable(ITable):
    _height: int = 60
    _width: int = 60
    _depth: int = 60 
    def get_dimensions(self):
        return self.__dict__
    
@dataclass    
class LargeTable(ITable):
    _height: int = 80
    _width: int = 80
    _depth: int = 80 
    def get_dimensions(self):
        return self.__dict__

class TableFactory:
    @staticmethod
    def get_table(type):
        if type == "s":
            return SmallTable()
        if type == "m":
            return MediumTable()
        if type == "l":
            return LargeTable()
        
CHAIR_SMALL = FunitureFatory.get_funiture("cs")
CHAIR_MEDIUM = FunitureFatory.get_funiture("cm")

print(CHAIR_SMALL.get_dimensions())
print(CHAIR_MEDIUM.get_dimensions())