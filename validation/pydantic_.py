import json
from pydantic import BaseModel,validator,root_validator
from typing import Optional



class ISBNMissingError(Exception):
    """Custom error that is raised when both ISBN10 and ISBN13 are missing."""
    def __init__(self,title:str , message:str) ->None:
        self.title = title
        self.message= message 
        super().__init__(message)

class ISBNFormatError(Exception):
    "Custom error that is raised when ISBN10 doesn't have the right format"

    def __init__(self,value:str , message:str) -> None:
        self.value = value
        self.message= message
        super().__init__(message)




class Book(BaseModel):
    title: str
    author: str
    publisher : str
    price: float
    isbn_10 : Optional[str]
    isbn_13: Optional[str] 
    subtitle: Optional[str]


    @root_validator(pre=True) #Specify whether it should validate it before they actually convert value into model before or after.
    @classmethod
    def check_isbn10_or_isbn13(cls,values): #values here will have all the attribute defined. 
        "Make sure there is either an isbn10 or isbn13 value defined."
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(title=values["title"],
            message = "Document should have either an ISBN10 or ISBN13" )
        return values



    @validator("isbn_10") #To act cleansing on isbb_10 attribute
    @classmethod
    def isbn_10_valid(cls,value): #value is assigned when json is mapped
        """Validator to check whether ISBN10 has a valid value."""
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) !=10:
            raise ISBNFormatError(value=value, message="ISBN10 should be 10 digits.")
        

        def char_to_int(char:str) -> int:
            #if it's X or x, return 10 otherwise simple conver them into its corresponding value.
            if char in "Xx":
                return 10
            return int(char)        
        weighted_sum = sum((10-i) * char_to_int(x) for i,x in enumerate(chars))
        if weighted_sum % 11 !=0:
            raise ISBNFormatError(
                value=value, message ="ISBN10 digit sum should be divisible by 11."
            )

    class Config:
        """Pydantic config class"""
        allow_mutation =False #This is going to make attribute immutable.
        anystr_upper = True

def main() -> None:

    with open('./validation/data.json') as file:
        data = json.load(file)
        books : list[Book] = [Book(**item) for item in data]

        #You can access data through .notation
        print(books[0].title)
    
        

if __name__ =="__main__":
    main()