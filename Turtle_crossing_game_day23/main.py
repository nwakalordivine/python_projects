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

screen.listen()

screen.onkey(player.move, "Up")
cars = []
game_is_on = True
while game_is_on:
    car_manager = CarManager()
    time.sleep(car_manager.more_speed)
    screen.update()

    # create multiple cars
    cars.append(car_manager)
    for all_cars in cars:
        all_cars.forward(20)

        # detect collision with car
        x_dist = abs(player.xcor() - all_cars.xcor())
        y_dist = abs(player.ycor() - all_cars.ycor())
        if all_cars.distance(player) < 20:
            scoreboard.game_over_text()
            game_is_on = False

    car_manager.move()

    # detects if the player successful pass through the cards
    if player.ycor() > 280:
        player.reset()
        car_manager.new_level()
        scoreboard.update()


screen.exitonclick()
