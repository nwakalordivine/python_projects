F_0 = 0
F_1 = 1

fibonacci_dictionary = {
    "fib_count": [0, 1, 1],
    "fibonacci": ["f0", "f1", "f2"]
}


def fib_range(fib_end):
    times = 0
    for fib in range(fib_end-2):
        new_fib = fibonacci_dictionary["fib_count"][1+times]+fibonacci_dictionary["fib_count"][2+times]
        fibonacci_dictionary["fib_count"].append(new_fib)
        fibonacci_dictionary["fibonacci"].append(f"f{2+2+times+1}")
        print(f"F{2+times+1} = {new_fib}")
        times += 1


def user_end():
    try:
        fib_end = int(input("f1 to f"))
        print("F0 = 0\nF1 = 1\nF2 = 1")
    except ValueError:
        print("input to which number you wish it to stop, should be a numeric number like '10'")
        fib_end = int(input("f1 to f"))
    fib_range(fib_end)


user_end()
