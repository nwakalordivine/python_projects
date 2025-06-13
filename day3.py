# Welcome to treasure island game
print('Welcome to treasure island')
# ask user to go either right or left
input_1 = input('right or left? ').lower()
# if user inputs left - continue
if input_1 == 'left':
    # ask user to either swim or wait
    input_2 = input('swim or wait? ').lower()
    # if user inputs wait - continue
    if input_2 == 'wait':
        # ask user to pick a door
        input_3 = input('pick a door: red blue or yellow? ').lower()
        # if user inputs yellow - user wins
        if input_3 == 'yellow':
            print('**You win**')
        # if user inputs red - game over
        elif input_3 == 'red':
            print('Game over, nice try tho!')
        # if user inputs blue - game over
        elif input_3 == 'blue':
            print('Game over')
        # if user inputs any other thing - invalid attempt
        else:
            print('invalid attempt')
    # if user inputs swim - game over
    elif input_2 == 'swim':
        print('Game over')
    # if user inputs any other thing - invalid attempt
    else:
        print('invalid attempt')
# if user inputs right - game over
elif input_1 == 'right':
    print('Game over')
# if user inputs any other thing - invalid attempt
else:
    print('invalid attempt!')
