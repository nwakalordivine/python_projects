from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_position = 10
        self.x_position = 10
        self.more_speed = 0.1

    def move_top_right(self):
        new_x = self.xcor() + self.x_position
        new_y = self.ycor() + self.y_position
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_position *= -1

    def bounce_x(self):
        self.x_position *= -1
        self.more_speed *= 0.9

    def reset_position(self):
        self.goto(x=0, y=0)
        self.more_speed = 0.1
        self.bounce_x()
