 #A python program to create a simple inventory dictionary
# Create an empty inventory dictionary

inventory = {}

# Function to add items to the inventory
def add_item():
    name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    # Add the item to the inventory with its quantity
    inventory[name] = quantity
    print("Item added successfully!")

# Function to update quantities of existing items
def update_quantity():
    name = input("Enter the item name: ")
    if name in inventory:
        quantity = int(input("Enter the new quantity: "))
        # Update the quantity of the item in the inventory
        inventory[name] = quantity
        print("Quantity updated successfully!")
    else:
        print("Item not found in inventory.")

# Function to retrieve information about a specific item
def retrieve_info():
    name = input("Enter the item name: ")
    if name in inventory:
        quantity = inventory[name]
        print(f"Item: {name}, Quantity: {quantity}")
    else:
        print("Item not found in inventory.")

# Function to calculate and display the total quantity of all items in the inventory
def calculate_total_quantity():
    total_quantity = sum(inventory.values())
    print(f"Total quantity of all items in the inventory: {total_quantity}")

# using a while loop to test the user input
while True:
    print("1. Add item to inventory")
    print("2. Update quantity of an item")
    print("3. Retrieve information about an item")
    print("4. Calculate total quantity of all items")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
#use a if---else statements 
    if choice == 1:
        add_item()
    elif choice == 2:
        update_quantity()
    elif choice == 3:
        retrieve_info()
    elif choice == 4:
        calculate_total_quantity()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")

