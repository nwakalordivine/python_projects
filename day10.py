from utilities2 import logo3


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


signs = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


def calculator():
    print(logo3)
    initial_number = float(input("What is the first number?: "))
    n1 = initial_number
    for sign in signs:
        print(sign)
    update = True
    while update:
        user_pick = input("Pick an operation: ")
        if user_pick in signs:
            n2 = float(input("What is the next number?: "))
            answer = signs[user_pick](n1, n2)
            print(f"{n1} {user_pick} {n2} = {answer}")
            reset = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation "
                          f"and 'q' to quit: ").lower()
            if reset == "y":
                n1 = answer
            elif reset == "n":
                print("\n"*20)
                calculator()
            elif reset == "q":
                print("Good bye")
                update = False
            else:
                if reset != ("y" or "n" or "q"):
                    print("invalid")
                    update = False
        else:
            print('invalid')


calculator()
