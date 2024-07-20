from tabulate import tabulate
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def turn_off():
    exit()


def coins_processor():
    quarters = int(input("Put the quarter Coin(s): "))
    dimes = int(input("Put the nickle Coin(s): "))
    nickles = int(input("Put the nickles Coin(s): "))
    pennies = int(input("Put the pennies Coin(s): "))

    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)


def coffe_order():
    user_order = input("\nWhat would you like? (espresso/latte/cappuccino):")
    water_required = 0
    milk_required = 0
    coffee_required = 0

    if user_order == "espresso":
        water_required = MENU[user_order]['ingredients']['water']
        coffee_required = MENU[user_order]['ingredients']['coffee']
        if water_required <= resources['water'] and coffee_required <= resources['milk']:
            resources['water'] -= water_required
            resources['coffee'] -= coffee_required
            coins = coins_processor()
            if coins == MENU['espresso']["cost"]:
                print("your coffee is getting ready")
            elif coins < MENU['espresso']["cost"]:
                print("Sorry that is not enough money!")
            elif coins > MENU['espresso']["cost"]:
                print(f"\nYour Coffee getting ready!")
                print(f"Total Bill = {MENU['espresso']["cost"]}")
                print(f"Here is your change: {round(coins - MENU['espresso']["cost"], 2)}")
        else:
            if water_required > resources['water']:
                print("Insufficient Water!!")
            if coffee_required > resources['milk']:
                print("insufficient Milk!!")

    elif user_order == "cappuccino":
        water_required = MENU[user_order]['ingredients']['water']
        milk_required = MENU[user_order]['ingredients']['milk']
        coffee_required = MENU[user_order]['ingredients']['coffee']
        if (water_required <= resources['water'] and milk_required <= resources['milk']
                and coffee_required <= resources['coffee']):
            resources['water'] -= water_required
            resources['coffee'] -= coffee_required
            resources['milk'] -= milk_required
            coins = coins_processor()
            if coins == MENU['espresso']["cost"]:
                print("your coffee is getting ready")
            elif coins < MENU['espresso']["cost"]:
                print("Sorry that is not enough money!")
            elif coins > MENU['espresso']["cost"]:
                print(f"\nYour Coffee getting ready!")
                print(f"Total Bill = {MENU['cappuccino']["cost"]}")
                print(f"Here is your change: {round(coins - MENU['espresso']["cost"], 2)}")
            else:
                if water_required > resources['water']:
                    print("Insufficient Water!!")
                if coffee_required > resources['milk']:
                    print("insufficient Milk!!")
        else:
            if water_required > resources['water']:
                print("Insufficient Water!!")
            if coffee_required > resources['milk']:
                print("insufficient Milk!!")
            if coffee_required > resources['coffee']:
                print("insufficient Coffee!!")

    elif user_order == "latte":
        water_required = MENU[user_order]['ingredients']['water']
        coffee_required = MENU[user_order]['ingredients']['coffee']
        milk_required = MENU[user_order]['ingredients']['milk']
        if (water_required <= resources['water'] and milk_required <= resources['milk']
                and coffee_required <= resources['coffee']):
            resources['water'] -= water_required
            resources['coffee'] -= coffee_required
            resources['milk'] -= milk_required
            coins = coins_processor()
            if coins == MENU['espresso']["cost"]:
                print("your coffee is getting ready")
            elif coins < MENU['espresso']["cost"]:
                print("Sorry that is not enough money!")
            elif coins > MENU['espresso']["cost"]:
                print(f"\nYour Coffee getting ready!")
                print(f"Total Bill = {MENU['latte']["cost"]}")
                print(f"Here is your change: {round(coins - MENU['espresso']["cost"], 2)}")
            else:
                if water_required > resources['water']:
                    print("Insufficient Water!!")
                if coffee_required > resources['milk']:
                    print("insufficient Milk!!")
        else:
            if water_required > resources['water']:
                print("Insufficient Water!!")
            if coffee_required > resources['milk']:
                print("insufficient Milk!!")
            if coffee_required > resources['coffee']:
                print("insufficient Coffee!!")
    else:
        print("Invalid Choice!, Try again.")


resources_table = [[key, value] for key, value in resources.items()]

machine_is_on = True
while machine_is_on:
    user_input = (input("\n🍵🍵🍵 Welcome to Coffe Machine 🍵🍵🍵\n\n1 - Order a coffee\n2 - To get resource report\n3 "
                        "- To turn off Coffee Machine\n\nEnter your choice: "))
    if user_input == "1":
        coffe_order()
    elif user_input == "2":
        print(tabulate(resources_table, headers=["Resource", "Remaining"], tablefmt="pretty"))
    elif user_input == "3":
        print("🍵 Coffee Machine shutting down!")
        machine_is_on = False
        turn_off()
    else:
        print("Invalid Choice Try again")
