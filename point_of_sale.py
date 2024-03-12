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

# Input sale details
item_id = input("Enter the item ID: ")
name = input("Enter the item name: ")
unit_price = float(input("Enter the unit price: "))
quantity = int(input("Enter the quantity: "))
# Loop until the user chooses to exit
# Determine the item type
while True:
    print("Choose the product type:")
    print("1. standard")
    print("2. discounted")
    print("3. service")
    print("4. Exit")
    item_type = int(input("Enter your choice (1/2/3/4): "))

    if item_type == 4:
        print("Exiting the program.")
        break

# Create an instance of the corresponding item type
if item_type == "1":
    item = StandardItem(item_id, name, unit_price)
    item.calculate_total()
elif item_type == "2":
    discount_percentage = float(input("Enter the discount percentage: "))
    item = DiscountedItem(item_id, name, unit_price, discount_percentage)
    item.calculate_total()
elif item_type == "3":
    hourly_rate = float(input("Enter the hourly rate: "))
    item = ServiceItem(item_id, name, hourly_rate)
    item.calculate_total()
else:
    print("Invalid item type.")
# Calculate and print total cost
if isinstance(item, ServiceItem):
    hours = int(input("Enter the number of hours: "))
    total_cost = item.calculate_total(hours)
else:
    total_cost = item.calculate_total(quantity)
    
print("Total cost:", total_cost)

