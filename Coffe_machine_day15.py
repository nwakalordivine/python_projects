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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_sufficiency_check(user_drink, order_requirement):
    """Checks if resources are sufficient for user choice and returns True if it is and False if it isn't """
    for key in user_drink["ingredients"]:
        if drink["ingredients"][key] > order_requirement[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def process_coin():
    """Processes the total money put in"""
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_transaction(user_payment, order_cost):
    """Checks if user payment is adequate, returns True when payment is adequate and give user change if any
     else it refunds user money and returns false"""
    if user_payment >= order_cost:
        user_change = user_payment - order_cost
        print(f"Here is ${round(user_change, 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredient):
    """Adds up profit after successful transaction and Deduct resources-used from available-resources"""
    global profit
    profit += drink["cost"]
    for key in order_ingredient:
        resources[key] -= order_ingredient[key]
    print(f"Here is your {drink_name} ☕️. Enjoy")


machine_on = True
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        resource_check = resource_sufficiency_check(drink, resources)
        if resource_check:
            total_coin = process_coin()
            if check_transaction(total_coin, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
