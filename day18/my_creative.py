import turtle as t
# import random

i = 5
tim = t.Turtle()
t.colormode(255)
tim.speed(0)
for _ in range(75):
    tim.circle(90, 365)
    tim.home()
    tim.right(i)
    i += 5

screen = t.Screen()
screen.exitonclick()

