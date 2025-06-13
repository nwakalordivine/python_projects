import random
# password letters, words and symbols for our password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('welcome to the password generator')

# ask user for preferred  no. of letters, symbols & numbers
user_input_1 = int(input('how many letters? '))
user_input_2 = int(input('how many numbers? '))
user_input_3 = int(input('how many symbols? '))
# get random numbers from the dedicated list per user's description
password = []
for nom in range(user_input_1):
    random_letters = random.choice(letters)
    password += random_letters
for nom in range(user_input_2):
    random_numbers = random.choice(numbers)
    password += random_numbers
for nom in range(user_input_3):
    random_symbols = random.choice(symbols)
    password += random_symbols
print(password)
random.shuffle(password)
updated_password = ''
for passw in password:
    updated_password += passw
print(f'your password is {updated_password}')

