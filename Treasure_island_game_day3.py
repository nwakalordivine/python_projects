print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road = input("you're at a cross road where do you want to go\nLeft or Right? ")
if road == "Right" or road == "RIGHT" or road == "right":
    print("there is shoot out, Game over!")
elif road == "Left" or road == "left" or road == "LEFT":
    print("you've crossed!")
    island = input("there is a lake with an island at the centre\nwould you like to Swim or Wait? ")
    if island == "swim" or island == "SWIM" or island == "Swim":
        print("you got eaten alive by a shark, Game over!")
    elif island == "wait" or island == "WAIT" or island == "Wait":
        print("the boat would be here shortly")
        door = input("you're at your dream house but you have to pick\nthe door"
                     " that is safest as the others\n would have"
                     " dangerous animals or insects, so pick either\nthe Red, Blue or Yellow door! ")
        if door == "Red" or door == "RED" or door == "red":
            print("they are harmful insects in this room, Game over!")
        elif door == "blue" or door == "BLUE" or door == "Blue":
            print("they are man eating animals in this room, Game over!")
        elif door == "yellow" or door == "Yellow" or door == "YELLOW":
            print("this door has all your hearts desires, well done You Won")
        else:
            print("kindly pick a valid option")
    else:
        print("kindly pick a valid option")
else:
    print("kindly pick a valid option")
