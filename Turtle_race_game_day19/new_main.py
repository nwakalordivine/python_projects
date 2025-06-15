import turtle as t
import random

screen = t.Screen()
screen.setup(width=1000, height=900)
is_race_on = False
players_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?, Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
random.shuffle(colors)
y = -250
for turtles in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-485, y=y)
    new_turtle.color(colors[turtles])
    y += 80
    all_turtle.append(new_turtle)

if players_bet:
    is_race_on = True

while is_race_on:
    for each_turtle in all_turtle:
        if each_turtle.xcor() > 468:
            winner = each_turtle.pencolor()
            if players_bet == winner:
                print(f"You've won!, the {winner} turtle is the winner")
            else:
                print(f"You've lost!, the {winner} turtle is the winner")
            is_race_on = False
        random_speed = random.randint(0, 10)
        each_turtle.forward(random_speed)

screen.exitonclick()
