# Initialize coffee menu with prices
coffee_menu = {
    "Latte": 15,
    "Cappuccino": 18,
    "Espresso": 12,
    "Macchiato": 20,
}

# Initialize constants
MAX_TOPPINGS = 3
TOPPING_COST = 1

def display_menu():
    print("Coffee Menu:")
    for coffee, price in coffee_menu.items():
        print(f"{coffee}: {price} AED")

def order_coffee():
    total_cost = 0
    order_details = []

    while True:
        display_menu()
        coffee_choice = input("Enter the coffee drink you want to order: ")
        if coffee_choice not in coffee_menu:
            print("Invalid coffee choice. Please choose from the menu.")
            continue

        quantity = int(input("Enter the quantity: "))
        size = input("Enter the size (Large, Medium, Small): ")
        toppings = []
        toppings_count = 0

        while toppings_count < MAX_TOPPINGS:
            topping = input(f"Add a topping (or 'done' to finish): ")
            if topping.lower() == 'done':
                break
            toppings.append(topping)
            toppings_count += 1

        coffee_cost = coffee_menu[coffee_choice] * quantity
        toppings_cost = len(toppings) * TOPPING_COST
        total_cost += (coffee_cost + toppings_cost)

        order_details.append(f"{quantity} {size} {coffee_choice} with {', '.join(toppings)}")

        more_orders = input("Do you want to order more drinks? (yes/no): ")
        if more_orders.lower() != 'yes':
            break

    print("Invoice:")
    for order in order_details:
        print(order)
    print(f"Total Cost: {total_cost} AED")

while True:
    print("Welcome to the Coffee Shop!")
    print("1. MENU for coffee drinks")
    print("2. Order a coffee drink")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_menu()
    elif choice == '2':
        order_coffee()
    elif choice == '3':
        print("Thank you for visiting! Have a great day.")
        break
    else:
        print("Invalid choice. Please choose from the menu.")
