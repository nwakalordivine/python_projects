import sys
# Had decided to build this bank ussd system in replica of Moniepoint ussd transaction flow (:
# # Built to simulate a Moniepoint-style bank USSD transaction system


def get_valid_number(prompt, length):
    """
    Prompt the user to enter a number of a specified length.
    Returns the number if it's valid (only digits and correct length).
    """
    while True:
        number = input(prompt)
        if number.isdigit() and len(number) == length:
            return number
        print(f"Invalid input. Please enter exactly {length} digits.")


def select_from_list(prompt, my_options):
    """
    Display a list of options and prompt the user to select one by index.
    Returns the index of the selected option.
    """
    print(prompt)
    for idx, option in enumerate(my_options, 1):
        print(f"{idx}> {option}")
    while True:
        try:
            selection = int(input("\n")) - 1
            if 0 <= selection < len(my_options):
                return selection
            print("Invalid input!")
        except ValueError:
            print("Enter a valid number.")


def set_transaction_pin():
    """
    Prompts the user to create a 4-digit transaction PIN.
    Returns the valid PIN.
    """
    while True:
        my_pin = input("Kindly set your Transaction PIN (4 digits): ")
        if my_pin.isdigit() and len(my_pin) == 4:
            return my_pin
        print("Invalid PIN. Must be 4 digits.")


def transfer_to_moniepoint(my_balance, my_pin):
    """
    Handles transferring funds to another Moniepoint account.
    Returns updated balance after the transaction.
    """
    amount = get_valid_amount()
    account = get_valid_number("Enter recipient's account number:\n", 10)
    total = amount
    return process_transaction(my_balance, my_pin, total, f"Transferring N{amount}.00 to {account}.")


def transfer_to_other_banks(my_balance, my_pin):
    """
    Handles transferring funds to accounts in other banks.
    Returns updated balance after the transaction.
    """
    amount = get_valid_amount()
    account = get_valid_number("Enter recipient's account number:\n", 10)
    bank = select_bank()
    fee = 20
    total = amount + fee
    return process_transaction(my_balance, my_pin, total, f"Transferring N{amount}.00 to {account} "
                                                          f"({bank}).\nFee: N{fee}")


def get_valid_amount():
    """
    Prompt the user to enter a valid amount (minimum 100).
    Returns the entered amount as integer.
    """
    while True:
        try:
            amount = int(input("Enter amount:\n"))
            if amount >= 100:
                return amount
            print("Amount too low (min: 100). Try again.")
        except ValueError:
            print("Enter a valid number.")


def process_transaction(my_balance, my_pin, total, message):
    """
    Validates PIN and processes the transaction if balance is sufficient.
    Returns the updated balance.
    """
    print(f"\n{message}\nTotal: N{total}.00\n")
    entered_pin = input("Enter PIN. Press 0 to go back:\n")
    if entered_pin == "0":
        return my_balance
    if entered_pin == my_pin:
        if total > my_balance:
            print("Insufficient funds!")
        else:
            my_balance -= total
            print(f"Transaction successful. Updated balance: N{my_balance}.00")
    else:
        print("Incorrect PIN!")
    return my_balance


def select_bank():
    """
    Displays paginated list of banks for user to select.
    Returns the selected bank name.
    """
    banks = [
        ["Access Bank", "GT Bank", "UBA", "FCMB"],
        ["Stanbic IBTC", "Fidelity Bank", "Sterling Bank", "Wema Bank"],
        ["Unity Bank", "Keystone Bank"]
    ]
    for page in banks:
        selection = select_from_list("Select Bank:", page + ["#>Next"])
        if selection < len(page):
            return page[selection]
    return banks[-1][select_from_list("Select Bank:", banks[-1])]


def buy_airtime(my_balance, my_pin, my_user_number, my_line):
    """
    Allows user to buy airtime for themselves or others.
    Applies a discount and processes transaction.
    Returns updated balance.
    """
    recipient, amount = select_airtime_recipient(my_user_number)
    discount = 10
    total = amount - discount
    return process_transaction(my_balance, my_pin, total, f"Buying N{amount}.00 {my_line}"
                                                          f" airtime for {recipient}. Discount: N{discount}")


def select_airtime_recipient(my_user_number):
    """
    Prompts user to choose between buying airtime for self or others.
    Returns recipient number and amount.
    """
    selection = select_from_list("Buy airtime:", ["For yourself", "For others"])
    if selection == 0:
        number = my_user_number
    else:
        number = get_valid_number("Enter recipient number:\n", 11)
    amount = get_valid_amount()
    return number, amount


def buy_data(my_balance, my_pin, my_user_number, my_line):
    """
    Allows user to buy data bundles for self or others based on network and plan type.
    Returns updated balance after the transaction.
    """
    selection = select_from_list("Buy data:", ["For yourself", "For others"])
    if selection == 0:
        recipient = my_user_number
        recipient_line = my_line
    else:
        recipient = get_valid_number("Enter recipient number:\n", 11)
        if recipient == my_user_number:
            print("Cannot use your number here!")
            return my_balance
        recipient_line = select_from_list("Pick recipient line:", ["MTN", "AIRTEL", "GLO", "9MOBILE"])

    data_type = ["Monthly", "Weekly", "Daily"]
    plan_group = select_from_list("Select data plan group:", data_type)
    network = ["MTN", "AIRTEL", "GLO", "9MOBILE"][recipient_line]

    data_plans = {
        "MTN": [["1.8GB - N1500", "2.7GB - N2000"], ["750MB - N500", "1.5GB - N1000"],
                ["100MB - N100", "200MB - N200"]],
        "AIRTEL": [["2GB - N1500", "3GB - N2000"], ["1GB - N500", "2GB - N1000"], ["150MB - N100", "300MB - N200"]],
        "GLO": [["2.5GB - N1500", "4GB - N2000"], ["1.2GB - N500", "2.4GB - N1000"], ["200MB - N100", "400MB - N200"]],
        "9MOBILE": [["2GB - N1500", "3.5GB - N2000"], ["800MB - N500", "1.5GB - N1000"],
                    ["120MB - N100", "250MB - N200"]]
    }

    selected_plan = select_from_list(f"Select {network} {data_type[plan_group]} plan:",
                                     data_plans[network][plan_group])
    price = int(data_plans[network][plan_group][selected_plan].split(" - N")[-1].replace(",", ""))
    return process_transaction(balance, my_pin, price,
                               f"Buying {data_plans[network][plan_group][selected_plan]} for {recipient} "
                               f"({network})")


def check_balance(my_balance, my_pin):
    """
    Checks and displays the user's balance if correct PIN is provided.
    Returns the (unchanged) balance.
    """
    if input("Enter PIN to check balance:\n") == my_pin:
        print(f"Your balance is N{my_balance}.00")
    else:
        print("Invalid PIN!")
    return my_balance


def change_pin(my_pin):
    """
    Allows the user to change their PIN after verifying the current one.
    Returns the new PIN if successful.
    """
    if input("Enter current PIN:\n") == my_pin:
        return set_transaction_pin()
    print("Incorrect PIN.")
    return my_pin


def block_account(my_pin):
    """
    Blocks the account after PIN verification and confirmation.
    Exits the program if user confirms.
    """
    if input("Enter PIN to block account:\n") != my_pin:
        print("Invalid PIN!")
        return
    if input("Are you sure? 1> Yes 2> No\n") == "1":
        print("Account blocked.")
        sys.exit()
    else:
        print("Action canceled.")


# MAIN EXECUTION
print("REGISTRATION FORM!")
balance = int(input("Input your Virtual Bank Amount (VBA) Balance!: "))
user_number = get_valid_number("Register a number to your bank:\n", 11)
line = ["MTN", "AIRTEL", "GLO", "9MOBILE"]
line_choice = select_from_list("Pick your mobile line:", line)
pin = set_transaction_pin()

print("\nTo end the program after any transaction, input 'quit'.\n")

if input("Input code (the code for this bank is '*5573#'): \n") == "*5573#":
    while True:
        print("\nWelcome to Moniepoint\n")
        options = [
            "Send to Moniepoint", "Send to other banks", "Buy airtime",
            "Buy data", "Check balance", "Change pin", "Block account"
        ]
        choice = input("\n".join([f"{i+1}> {opt}" for i, opt in enumerate(options)]) + "\n\n").lower()
        if choice == "1":
            balance = transfer_to_moniepoint(balance, pin)
        elif choice == "2":
            balance = transfer_to_other_banks(balance, pin)
        elif choice == "3":
            balance = buy_airtime(balance, pin, user_number, line[line_choice])
        elif choice == "4":
            balance = buy_data(balance, pin, user_number, line_choice)
        elif choice == "5":
            balance = check_balance(balance, pin)
        elif choice == "6":
            pin = change_pin(pin)
        elif choice == "7":
            block_account(pin)
        elif choice == "quit":
            print(f"Thank you for using our services. Your balance is N{balance}.00")
            break
        else:
            print("Invalid input.")
else:
    print("Invalid USSD code!")
