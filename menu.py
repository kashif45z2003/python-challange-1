# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Order list to store customer order details
order = []

# Start the ordering process
print("Welcome to the variety food truck.")

place_order = True
while place_order:
    # Display menu categories
    print("From which menu would you like to order?")
    
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get customer's selected category
    menu_category = input("Type menu number: ")
    if menu_category.isdigit() and int(menu_category) in menu_items.keys():
        menu_category_name = menu_items[int(menu_category)]
        print(f"You selected {menu_category_name}")
        
        # Display items in the chosen category
        print(f"What {menu_category_name} item would you like to order?")
        i = 1
        category_items = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    item_name = f"{key} - {sub_key}"
                    category_items[i] = {"Item name": item_name, "Price": sub_value}
                    print(f"{i}      | {item_name:<24} | ${sub_value:.2f}")
                    i += 1
            else:
                category_items[i] = {"Item name": key, "Price": value}
                print(f"{i}      | {key:<24} | ${value:.2f}")
                i += 1

        # Get customer's selected item
        item_number = input("Type item number to order: ")
        if item_number.isdigit() and int(item_number) in category_items:
            selected_item = category_items[int(item_number)]
            item_name = selected_item["Item name"]
            item_price = selected_item["Price"]

            # Get quantity of the selected item
            quantity = input(f"How many {item_name} would you like? ")
            quantity = int(quantity) if quantity.isdigit() else 1

            # Add item to order
            order.append({"Item name": item_name, "Price": item_price, "Quantity": quantity})
            print(f"Added {quantity} x {item_name} to your order.")
        else:
            print("You didn't select a valid menu item.")
    else:
        print("You didn't select a valid menu option.")

    # Check if customer wants to continue ordering
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()
        if keep_ordering == 'n':
            place_order = False
            break
        elif keep_ordering == 'y':
            break
        else:
            print("Please type 'Y' or 'N'.")

# Print the final order summary
print("\nThis is what we are preparing for you.")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
# Calculate total cost using list comprehension
total_cost = sum([item["Price"] * item["Quantity"] for item in order])

# Print each item in the order
for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    print(f"{item_name:<24} | ${price:.2f} | {quantity}")
