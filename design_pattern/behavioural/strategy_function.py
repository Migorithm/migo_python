"""
The same functionality of class-based strategy design pattern can be implemented with less code by using functions.
"""
from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Callable, NamedTuple

class Customer(NamedTuple):
    name: str
    fidelity:str
    
class LineItem(NamedTuple):
    product:str
    quantity:int
    price:Decimal
    
    def total(self) -> Decimal:
        return self.price * self.quantity

@dataclass(frozen=True)
class Order:
    """
    The context
    """
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'],Decimal]] = None
    
    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))
    
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self) # Why self.promotion(self)? promotion is not a method, it's an instance attribute taht happens to be callable. 
        return self.total() - discount
    
    def __repr__(self):
        return f"<Order total: {self.total():.2f} due: {self.due():2f}>"

def fidelity_promo(order:Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity points."""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)

def bulk_item_promo(order:Order) -> Decimal:
    """10% discount for each LineItem with 20 or more units."""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount

def large_order_promo(order:Order) -> Decimal:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)

def best_promo(order: Order) -> Decimal:
    """ Compute the best discount available"""
    return max(promo(order) for promo in [fidelity_promo,bulk_item_promo,large_order_promo])
