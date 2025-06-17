import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create multiple cars
    car_manager.create_new_car()
    car_manager.move()

    # detect collision with car
    for car in car_manager.segments:
        if car.distance(player) < 20:
            scoreboard.game_over_text()
            game_is_on = False

    # detects if the player successful pass through the cards
    if player.ycor() > 280:
        player.reset()
        car_manager.new_level()
        scoreboard.score += 1
        scoreboard.update()


screen.exitonclick()
