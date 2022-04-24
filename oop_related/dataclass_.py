# This module provides a decorator and functions for 
# automatically adding generated special methods such as 
# __init__() and __repr__() to user-defined classes.


from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
# The above is the same as 
"""
def __init__(self, name:str , unit_price:float, quantity_on_hand:int =0)
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
"""

#Addtional parameter can be thrown
@dataclass()
class C:
    pass

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False)
class C:
    pass

#where init and repr are set to default True
