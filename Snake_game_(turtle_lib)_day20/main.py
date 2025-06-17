from turtle import Screen
import time
from snake_class import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()

    # Detect collision with wall.
    if x_cor > 280 or x_cor < -280 or y_cor > 280 or y_cor < -280:
        score_board.reset()
        snake.reset()
        score_board.update()

    # Detect collision with tail.
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()


screen.exitonclick()
