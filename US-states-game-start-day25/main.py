from turtle import Turtle, Screen
import pandas
import time

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
my_image = "blank_states_img.gif"
screen.addshape(my_image)
screen.tracer(0)
turtle.shape(my_image)

is_not_complete = True
score = 0

correct_guesses = []
while is_not_complete:
    screen.update()
    time.sleep(0.5)
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()

    if score != 0:
        play_answer = screen.textinput(title=f"{score}/50 states correct", prompt="What's another state's name").title()
    else:
        play_answer = screen.textinput(title="Guess the state", prompt="What's another state's name").title()

    data = pandas.read_csv("50_states.csv")

    if play_answer == "Exit":
        missed_states_list = [missed_states for missed_states in data.state.to_list()
                              if missed_states not in correct_guesses]
        states_missed = pandas.DataFrame(missed_states_list)
        states_missed.to_csv("states-to-learn.csv")
        break

    if play_answer in data.state.to_list():
        u_states = data[data.state == play_answer]
        x_cor = int(u_states.x.iloc[0])
        y_cor = int(u_states.y.iloc[0])
        new_turtle.goto(x=x_cor, y=y_cor)
        new_turtle.write(arg=play_answer, align="center", font=("Arial", 8, "normal"))
        if play_answer not in correct_guesses:
            correct_guesses.append(play_answer)
            score += 1
    else:
        pass

    if score == 50:
        is_not_complete = False
