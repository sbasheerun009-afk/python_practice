class Order:
    def __init__(self,order_id,amount):
        self.order_id = order_id
        self.amount = amount 
        
    def final_bill(self):
        return self.amount

class Vegorder(Order):
    def final_bill(self):
        return self.amount + (self.amount * 0.05)
class Nonvegorder(Order):
    def final_bill(self):
        return self.amount + (self.amount * 0.012)
class Dessertorder(Order):
    def final_bill(self):
        return self.amount + (self.amount * 0.18)
orders = Order[Vegorder(102,400),Nonvegorder(102,500),Dessertorder(103,600),Vegorder(104,450)]
print("final order is:")
for order in orders:
    print(f"orderId:{order.order_id},final_bill{order.final_bill()}")
