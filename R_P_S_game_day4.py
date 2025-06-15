import random
# Rock Paper Scissors Game

rock = """
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
diagram = [rock, paper, scissors]

# user picks either 0, 1, 2
user_input = int(input('What do you choice, 0 for rock, 1 for paper, or 2 scissors: '))

# if user input is not 0, 1 or 2 - invalid attempt
if user_input == 0 or user_input == 1 or user_input == 2:
    print(diagram[user_input])
    computer_input = random.randint(0, 2)

    print(f'Computer choice:\n{diagram[computer_input]}')
    if user_input == computer_input:
        print('its a draw')
    # if user input 0, 1, 2 and computer input 2, 0, 1 - you win
    elif user_input == 0 and computer_input == 2:
        print('you win')
    elif user_input == 1 and computer_input == 0:
        print('you win')
    elif user_input == 2 and computer_input == 1:
        print('you win')
    # if user input 2, 0, 1 and computer input 0, 1, 2 - you lose
    elif user_input == 2 and computer_input == 0:
        print('you lose')
    elif user_input == 0 and computer_input == 1:
        print('you lose')
    elif user_input == 1 and computer_input == 2:
        print('you lose')

else:
    print('invalid attempt')
