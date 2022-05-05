class Order:
    def __init__(self,cart,customer):
        self.cart = list(cart)
        self.customer = customer
    def __bool__(self):
        return len(self.cart) > 0


order1 = Order(['banana', 'apple', 'mango'], 'Real Python')
order2 = Order([], 'Python')

for order in [order1, order2]:
    if order:
        print(f"{order.customer}'s order is processing...")
    else:
        print(f"Empty order for customer {order.customer}")