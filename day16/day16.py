from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while True:
    choice = input(f"What would you like ({menu.get_items()}): ").lower().strip()

    if choice == 'off':
        quit()
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        check = menu.find_drink(choice)
        if not check:
            continue
        is_enough = coffee_maker.is_resource_sufficient(check)
        if not is_enough:
            continue
        if not money_machine.make_payment(check.cost):
            continue
        coffee_maker.make_coffee(check)
