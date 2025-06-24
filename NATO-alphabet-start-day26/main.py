import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

while True:
    user_word = input("Enter a word: ").upper()
    user_list = [letters for letters in user_word]
    try:
        user_word_list = [nato_dict[letter] for letter in user_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(user_word_list)
        go_again = input('\n\n\nWould you like to try again? (y/n): ').lower()
        if go_again != "y" and go_again != "n":
            raise TypeError(f"your entry '{go_again}' is invalid")
        if go_again == "y":
            pass
        else:
            break

