import random
from utilities2 import data, logo6, vs


def space_logo():
    """Takes care of the restart space and logo print"""
    print("\n"*20)
    print(logo6)


#  use the two generated numbers to get the respective person's information from game_data.py
#  and access there respective following
def person_info(person):
    """Takes generated numbers to identification of comparing persons"""
    compare_a = ""
    if person == person_a:
        compare_a = "A"
    elif person == person_b:
        compare_a = "B"
    return (f"Compare {compare_a} :{data[person]["name"]}, a {data[person]["description"]}, "
            f"from {data[person]["country"]}.")


# generate two random numbers between 0 - 49
def generate_num():
    """Generates random numbers responsible for picking persons to be compared"""
    random_person = random.randint(0, 49)
    return random_person


# compare and determine which has a greater following
def compare_followers():
    """Compares and determine if user picked correctly and response True or False"""
    if user_pick == "a":
        if a > b:
            return True
        elif b > a:
            return False
        elif a == b:
            print("You're right! Though it's a draw")
            return True
    elif user_pick == "b":
        if b > a:
            return True
        elif a > b:
            return False
        elif b == a:
            print("You're right! Though it's a draw")
            return True


def following(person_1, person_2):
    """Sorts out a and b's following number"""
    first = data[person_1]["follower_count"]
    second = data[person_2]["follower_count"]
    return first, second


person_a = generate_num()
person_b = generate_num()
if person_a == person_b:
    person_b = generate_num()

a, b = following(person_a, person_b)
score = 0
print(logo6)

win_lose = True
while win_lose is True:
    a, b = following(person_a, person_b)
    print(f"{person_info(person_a)}\n{vs}\n{person_info(person_b)}")
    user_pick = input("Who has more followers? Type 'A' or 'B': ").lower()
    win_lose = compare_followers()
    if win_lose is True:
        score += 1            # create a score variable that adds +1 when ever the user is correct
        space_logo()
        print(f"You're right! Current score: {score}")
    if win_lose is True and user_pick == "a":
        person_a = person_b
        person_b = generate_num()
    elif win_lose is True and user_pick == "b":
        person_a = person_b
        person_b = generate_num()
    elif win_lose is False:
        space_logo()
        print(f"Sorry, that's wrong. Final score: {score}")
