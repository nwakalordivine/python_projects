import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.segments = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_new_car(self):
        car = random.randint(1, 6)
        if car == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_cor = random.randint(-240, 250)
            x_cor = 300
            new_car.goto(x=x_cor, y=y_cor)
            self.segments.append(new_car)

    def move(self):
        for cars in self.segments:
            cars.backward(STARTING_MOVE_DISTANCE)

    def new_level(self):
        self.car_speed += MOVE_INCREMENT
