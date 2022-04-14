from pydantic import BaseModel,Field
from typing import Optional


class Car(BaseModel):
    make: str
    year: int = Field(1971,ge=1970) #default value 
    # model: str
    # price: float
    # engine: Optional[str] = "V4" #Default value
    # autonomous: bool
    # sold: list[str]
    
a= Car(make="st",year=1999)
b= Car(make="ss")
print(a,b)