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

order = []
print("Welcome to Lu's!")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")

        # Store the menu category associated with its menu item number
        menu_items[i] = key

        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():

        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():

            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]

            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            # Formatting follows same convention as below
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            menu_selection = input("Please enter menu item number: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]["Item name"]
                    item_price = menu_items[menu_selection]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity_input = input(f"How many {item_name} would you like? (Default is 1) ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity_input.isdigit():
                        quantity = int(quantity_input)
                    else:
                        quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order.append({
                    "Item name": item_name,
                    "Price": item_price,
                    "Quantity": quantity
                     })
                    print(f"Added {quantity} {item_name} to your order.")
                else:
                    # Tell the customer that their input isn't valid
                    print(f"{menu_selection} wasn't on the menu - please try again.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number - please try again.")

    while True:
        # Ask the customer if they would like to order anything else
        # Added .lower() for cleaner inputs - this also covers 2 match cases
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()


        # 5. Checking the customer's input
        # Using match case to handle customer input vs if-else
        match keep_ordering:
            case 'y':
                # Continue ordering
                place_order = True
                break
            case 'yes':
                # Added this for my own sanity
                place_order = True
                break
            case 'n':
                # Complete the order
                place_order = False
                print("Thank you for your order!")
                break
            case 'no':
                # Complete the order
                place_order = False
                print("Thank you for your order!")
                break
            case _:
                # If they enter something other than Y or N
                print("That wasn't an answer! Please try again.")

# Print out the customer's order
print("\nThis is what we're preparing for you:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
total_price = 0
for item in order:
    # 7. Store the dictionary items as variables
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # 8 / 9 Formatted space string
    print(f"{item_name:<25}| ${price:>6.2f} | {quantity:>3}")

    # 11. Calculate the cost of the order using list comprehension
    # Multiply the price by quantity for each item in the order list, then sum()
    # Print the total price
total_price = sum(item["Price"] * item["Quantity"] for item in order)
print(f"\nTotal Price: ${total_price:.2f}")
print("Thanks for stopping at Lu's!")
