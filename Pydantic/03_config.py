from pydantic import BaseModel,Field,validator


class Car(BaseModel):
    make:str
    year:int = Field(ge=1970,le=2022)
    
    @validator("make",allow_reuse=True)
    @classmethod
    def make_valid(cls,value):
        if value not in ("Hyundai","Kia"):
            raise ValueError("Given value not acceptable")
        return value
    
carA = Car(make="Hyundai",year=2000)
print(carA)

carA.make = "Honda" #Changeable! 
print(carA)  #make='Honda' year=2000




class Car(BaseModel):
    make:str
    year:int = Field(ge=1970,le=2022)
    
    @validator("make",allow_reuse=True)
    @classmethod
    def make_valid(cls,value):
        if value not in ("Hyundai","Kia"):
            raise ValueError("Given value not acceptable")
        return value

    class Config:
        """Pydantic config class"""
        allow_mutation= False
        allow_reuse=True
        
carA = Car(make="Hyundai",year=2000)
print(carA)

carA.make = "Honda" #Changeable! 
print(carA)  #  "Car" is immutable and does not support item assignment
