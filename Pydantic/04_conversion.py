from pydantic import BaseModel,Field,validator

class Car(BaseModel):
    make:str
    year:int = Field(ge=1970,le=2022)
    
    @validator("make")
    @classmethod
    def make_valid(cls,value):
        if value not in ("Hyundai","Kia"):
            raise ValueError("Given value not acceptable")
        return value

    class Config:
        """Pydantic config class"""
        allow_mutation= False
        
carA = Car(make="Hyundai",year=2000)
print(carA)

#Conversion to dict!
b= carA.dict()

b["make"] = "Kia"

b= Car(**b) 
print(b)



print(b.dict(exclude={"make"})) #You can exclude a certain value.
print(b.dict(include={"year"})) #You can select a certain field as well.


