#A python program for an inventory management system
import datetime#we import datetime
#create a class product
class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):#initialize the atributes
        self.product_id = product_id
        self.product_name = product_name
        self.quantity_in_stock = quantity_in_stock
    
    def calculate_value(self):#this is a method
        return self.quantity_in_stock
#child class of product
class SimpleProduct(Product):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price):
        super().__init__(product_id, product_name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price
#child class of simpleProducts
class PerishableProduct(SimpleProduct):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, product_name, quantity_in_stock, unit_price)
        self.expiry_date = expiry_date

    def calculate_value(self, shelf_life):
        shelf_life_remaining = (self.expiry_date - datetime.datetime.now()).days
        discount_factor = shelf_life_remaining / shelf_life
        total_value = self.quantity_in_stock * self.unit_price
        discounted_value = total_value * discount_factor
        return discounted_value
 #child class of Product       
class DigitalProduct(Product):
    def __init__(self, product_id, product_name, quantity_in_stock, price):
        super().__init__(product_id, product_name, quantity_in_stock) 
        self.price = price

    def calculate_value(self):
        return self.quantity_in_stock * self.price

# use while Loop until the user chooses to exit
while True:
    print("Choose the product type:")
    print("1. Simple")
    print("2. Perishable")
    print("3. Digital")
    print("4. Exit")
    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 4:
        print("Exiting the program.")
        break
#prompt the user to enter the name,product id and the quantity
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
#if_else statements are used to test the choice of the user
    if choice == 1:
        unit_price = float(input("Enter unit price: "))
        product = SimpleProduct(product_id, name, quantity, unit_price)
        total_value = product.calculate_value()
    elif choice == 2:
        unit_price = float(input("Enter unit price: "))
        expiry_date = datetime.datetime.strptime(input("Enter expiry date (YYYY-MM-DD): "), "%Y-%m-%d")
        shelf_life = float(input("Enter shelf life (in days): "))
        product = PerishableProduct(product_id, name, quantity, unit_price, expiry_date)
        total_value = product.calculate_value(shelf_life)
    elif choice == 3:
        price = float(input("Enter price: "))
        product = DigitalProduct(product_id, name, quantity, price)
        total_value = product.calculate_value()
    else:
        print("Invalid choice.")
        continue
    #print the total value 
    print("Total value of product:", total_value)

