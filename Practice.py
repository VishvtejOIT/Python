class Bill:
    def __init__(self, items):
        self.items = items
    
    def calculate_total(self):
        total = sum([item[1] for item in self.items])
        return total

class DiscountedBill(Bill):
    def __init__(self, items, discount_rate):
        super().__init__(items)
        self.discount_rate = discount_rate
    
    def calculate_total(self):
        total = super().calculate_total()
        discount = total * self.discount_rate / 100
        discounted_total = total - discount
        return discounted_total

items = [
        ("Pizza", 15.0),
        ("Pasta", 12.0),
        ("Salad", 7.0),
        ("Drink", 3.0)
]
    
regular_bill = Bill(items)
print(f"Regular Bill Total: ${regular_bill.calculate_total():.2f}")
    
discounted_bill = DiscountedBill(items, 10)
print(f"Discounted Bill Total (10% discount): ${discounted_bill.calculate_total():.2f}")