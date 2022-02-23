"""
The properties of an enumeration are useful for defining an immutable, 
related set of constant values that may or may not have a semantic meaning.
"""

from enum import Enum , auto
from dataclasses import dataclass 


class Role(Enum):
    """Employee roles."""
    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()

@dataclass
class Employee:
    """ Basic representation of an employee at the company"""
    name: str
    role: Role


"""
Usecase of Enum:
Imagine that the role of Employee class was string type. 
And as string can be any letters, people who type in might not know
What value they have to put. 

To narrow down variability, we fix what roles are available
by using Enum.

    
"""

for i in Role:
    print(i)
    
    
emp_1 = Employee("John",Role.MANAGER)
emp_2 = Employee("King",Role.PRESIDENT)
print(emp_1 , emp_2)