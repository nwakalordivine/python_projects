import random
from utilities2 import image, logo, word_list


print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

place_holder = ''
for blanks in range(len(chosen_word)):
    place_holder += '_'
print(place_holder)
game_over = False
correct_word = []
lives = 6
while game_over is False:
    guess = input('guess a letter: ')

    if len(guess) == 1:
        if guess in correct_word:
            print(f"you've guessed the word '{guess}' already")

        display = ''
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_word.append(guess)
            elif letter in correct_word:
                display += letter
            else:
                display += '_'
        print(f'Word to guess: {display}')

        if guess not in chosen_word:
            print(f"you guess '{guess}' is not in the word")
            lives -= 1
            if lives == 0:
                game_over = True
                print(f"the correct word was '{chosen_word}'")
                print('you lose')

        if '_' not in display:
            game_over = True
            print('you win')

        print(image[lives])
    else:
        print('you can only attempt one letter at a time\n')
