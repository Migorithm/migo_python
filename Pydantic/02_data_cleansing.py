import json
from pydantic import BaseModel, Field ,validator
from typing import Optional
a = json.load(open("./cars.json")) #array of dictionarys


class PriceError(Exception):
    """Custom error that is raised when the price is too low"""
    def __init__(self,value:float, message:str)-> None:
        self.value= value
        self.message=message
        super().__init__(message)


class Car(BaseModel):
    make:str 
    model:str
    year:int = Field(...,ge=1970)
    price: float
    engine: str 
    autonomous:bool
    sold:Optional[list[str]]
    
    @validator("price")
    @classmethod
    def price_valid(cls,value):
        if value < 50000:
            raise PriceError(value=value,message="Price is too low to be true")
        return value

cars:list[Car] = [Car(**item) for item in a]
print(cars)