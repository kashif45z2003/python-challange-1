# Step 1: Initialize the order list
order_list = []

# Step 2: Define the menu
menu = {
    1: {"name": "Burger", "price": 5.00},
    2: {"name": "Fries", "price": 2.50},
    3: {"name": "Soda", "price": 1.75}
}

# Step 3: Start order-taking loop
while True:
    # Prompt for item selection
    try:
        item_num = int(input("Enter the item number you want to order (1 for Burger, 2 for Fries, 3 for Soda): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    
    # Check if the item exists in the menu
    if item_num not in menu:
        print("Item not found in the menu. Please try again.")
        continue
    
    # Retrieve item details
    item_name = menu[item_num]["name"]
    item_price = menu[item_num]["price"]

    # Prompt for quantity
    try:
        quantity = int(input(f"Enter quantity for {item_name} (default is 1 if invalid): "))
        if quantity <= 0:
            raise ValueError  # To handle negative or zero quantities
    except ValueError:
        quantity = 1

    # Append the item to the order list
    order_list.append({"name": item_name, "price": item_price, "quantity": quantity})
    print(f"Added {quantity} x {item_name} to your order.")

    # Ask if the user wants to keep ordering
    keep_ordering = input("Do you want to add another item? (Y/N): ").strip().upper()
    if keep_ordering == "N":
        break
    elif keep_ordering != "Y":
        print("Invalid input, assuming you want to keep ordering.")

# Step 4: Generate and print the receipt
print("\nOrder Receipt")
print("-" * 30)
total_price = 0

for item in order_list:
    # Calculate total for this line
    line_total = item["price"] * item["quantity"]
    total_price += line_total

    # Format the line for the receipt
    print(f"{item['name']:10} x {item['quantity']:2} @ ${item['price']:.2f} each = ${line_total:.2f}")

print("-" * 30)
print(f"Total Price: ${total_price:.2f}")


