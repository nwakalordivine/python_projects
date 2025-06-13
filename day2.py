# Tip calculator
print('Tip calculator')
# user inputs
bill = int(input('What is your bill? $ '))
tip = int(input('How much percentage tip would you like to put? '))
number_of_people = int(input('how many people are to split the bill with you? '))
# tip is added
tip_calculation = (tip/100) * bill
tip_plus_bill = tip_calculation + bill
# bill is slit amongst the number of people
amount_paid_per_person = tip_plus_bill/number_of_people
# result
print(f'Amount to be paid per person is ${amount_paid_per_person}')
