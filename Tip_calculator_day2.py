# Tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15 "))
people = int(input("How many people to split the bill? "))
stat = (tip / 100) * bill
final = bill + stat
spread = final / people
total_final = round(spread, 2)
print(f"Each person should pay: $ {total_final}")
