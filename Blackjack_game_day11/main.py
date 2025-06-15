import random
from utilis import logo


def deal_up():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards):
    added_list = sum(list_of_cards)

    if added_list == 21 and len(list_of_cards) == 2:
        return 0

    elif 11 in list_of_cards and added_list > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = [deal_up(), deal_up()]
    computer_cards = [deal_up(), deal_up()]
    user_score = 0
    computer_score = 0

    is_game_over = False
    while is_game_over is False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards {user_cards}, current score: {user_score}")
        print(f"computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            add_up = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if add_up == "y":
                user_cards.append(deal_up())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_up())
        computer_score = calculate_score(computer_cards)

    print(f"your cards {user_cards}, final score: {user_score}")
    print(f"computer cards: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n"*20)
    play_game()
