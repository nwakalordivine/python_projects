import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.hideturtle()

tim.penup()
list_of_colours = [(203, 34, 66), (71, 116, 151), (228, 161, 193),
                   (150, 184, 70), (151, 160, 164), (242, 235, 46), (37, 161, 80), (35, 31, 32), (137, 205, 187),
                   (240, 99, 54), (75, 65, 40), (33, 162, 165), (221, 49, 65), (142, 210, 191)]


tim.penup()
for _ in range(2):
    tim.right(90)
    tim.forward(250)
tim.left(180)

loop_control = 10
i = 10
while loop_control < 110:
    for _ in range(i):
        tim.dot(20, random.choice(list_of_colours))

        tim.speed(0)
        tim.forward(50)

    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.setheading(360)
    loop_control += 10



screen = t.Screen()
screen.exitonclick()

