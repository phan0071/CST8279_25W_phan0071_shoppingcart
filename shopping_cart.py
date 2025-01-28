# Student name: Andrea Phan
# Due date: Jan 28, 2025

#This program simulates a simple shopping cart. Users can add items, specify quantities, and see the total cost.
# The program uses exception handling to manage invalid inputs.

print("Welcome to the Shopping Cart Program!")

# Ask the user for the number of items, price, and cost of each item

while True:
    total_cost = float()
    price = int(input("How many items would you like to purchase?"))

    while price > 0:

        try:
            input("Please enter the name of the item you would like to purchase?")
            item_price = float(input("What is the price of the item you would like to purchase?"))
            item_quantity = int(input("How many of the items would you like to purchase?"))
            item_cost = float(item_price * item_quantity)
            total_cost += item_cost
            price = price - 1
        except ValueError:
            print("Error: Your input is invalid. Please retype the item information.")
            continue
    
    print('Your total cost is ', total_cost)
    
    restart = input("\nWould you like to restart the program? (Yes/No): ")
    if restart == 'No':
        print("\nThank you for shopping with us!")
        break
