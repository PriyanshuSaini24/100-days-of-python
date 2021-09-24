import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def remove_resources(coffee):
    resources['water'] -= coffee['ingredients']['water']
    resources['milk'] -= coffee['ingredients']['milk']
    resources['coffee'] -= coffee['ingredients']['coffee']


def coins(drink_choice, coffee_choice):
    print(f"Your drink costs ${drink_choice['cost']}")
    print("Please insert coins")
    quarters = float(input("how many quarters? ($0.25) "))
    dimes = float(input("how many dimes? ($0.10) "))
    nickels = float(input("how many nickles? ($0.05) "))
    pennies = float(input("how many pennies? ($0.01) "))
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if total_money < drink_choice['cost']:
        print("Sorry that's not enough money")
        welcome()
    elif total_money > drink_choice['cost']:
        change = total_money - drink_choice['cost']
        resources["money"] += drink_choice['cost']
        remove_resources(drink_choice)
        print(f"Here is ${change:.2f} in change. ")
        print(f"Making your {coffee_choice}... ")
        time.sleep(1)
        print("here you go! ☕")
    else:
        resources["money"] += drink_choice['cost']
        remove_resources(drink_choice)
        print(f"Making your {coffee_choice}... ")
        time.sleep(1)
        print("here you go! ☕")


def check_resources(drink, coffee_choice):
    if resources["water"] < drink["ingredients"]["water"]:
        print("not enough water")
        welcome()
    elif resources["milk"] < drink["ingredients"]["milk"]:
        print("not enough milk")
        welcome()
    elif resources["coffee"] < drink["ingredients"]["coffee"]:
        print("not enough coffee")
        welcome()
    else:
        coins(drink, coffee_choice)


def welcome():
    resources['money'] = 0
    print("Booting up...")
    time.sleep(1)
    off = False
    while not off:
        choice = input("what would you like? (espresso/latte/cappuccino/report)"
                       "\nor turn me off by saying 'off': ")
        if choice == "espresso":
            coffee = 'espresso'
            (check_resources(MENU[choice], coffee))
        elif choice == "latte":
            coffee = 'latte'
            (check_resources(MENU[choice], coffee))
        elif choice == "cappuccino":
            coffee = 'cappuccino'
            (check_resources(MENU[choice], coffee))
        elif choice == "report":
            for key, value in resources.items():
                print(f"{key}:", value)
        elif choice == "off":
            print("Shutting down...")
            time.sleep(1)
            print("Goodbye")
            off = True


welcome()
