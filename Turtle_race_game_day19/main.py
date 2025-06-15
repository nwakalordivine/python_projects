import turtle as t


tim = t.Turtle()
screen = t.Screen()
tim.speed(0)


def move_forwards():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_counter_clockwise():
    tim.right(10)


def move_anti_clock_wise():
    tim.left(10)


def clear_drawings():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_anti_clock_wise)
screen.onkey(key="c", fun=clear_drawings)
screen.exitonclick()
