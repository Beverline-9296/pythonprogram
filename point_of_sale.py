#A python program to calculate the the point of sale
# Create the class and subclasses
class SaleItem:
    def __init__(self, item_id, name, unit_price):#initializre the parameters
        self.item_id = item_id
        self.name = name
        self.unit_price = unit_price
#create a method
    def calculate_total(self, quantity):
        # return the total cost of a given quantity of an item
        return self.unit_price * quantity
    
#Child class   
class StandardItem(SaleItem):
    def __init__(self, item_id, name, unit_price):
        super().__init__(item_id, name, unit_price)

    def calculate_total(self, quantity):
#computes the total cost by multiplying the quantityby unit price
     total_cost = super().calculate_total(quantity)
     return total_cost


class DiscountedItem(SaleItem):
    def __init__(self, item_id, name, unit_price, discount_percentage):
        super().__init__(item_id, name, unit_price)
        self.discount_percentage = discount_percentage

    def calculate_total(self, quantity):
        total_cost = super().calculate_total(quantity)
        discounted_cost = total_cost * (1 - self.discount_percentage / 100)
        return discounted_cost


class ServiceItem(SaleItem):
    def __init__(self, item_id, name, hourly_rate):
        super().__init__(item_id, name, hourly_rate)
        self.hourly_rate = hourly_rate

    def calculate_total(self, hours):
        total_cost = self.hourly_rate * hours
        return total_cost

https://github.com/Beverline-9296/pythonprogram.git
