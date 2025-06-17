import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.y_cor = random.randint(-240, 250)
        self.x_cor = 300
        self.goto(x=self.x_cor, y=self.y_cor)
        self.setheading(180)
        self.more_speed = 0.3

    def move(self):
        self.forward(20)

    def reset(self):
        self.goto(x=self.x_cor, y=self.y_cor)

    def new_level(self):
        self.more_speed *= 0.9