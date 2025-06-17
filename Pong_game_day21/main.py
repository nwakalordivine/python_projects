from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

score_board = ScoreBoard()


game_on = True
while game_on:
    time.sleep(ball.more_speed)
    screen.update()
    ball.move_top_right()

    # detect ball collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect ball collision with paddles
    if ball.distance(l_paddle) < 60 and ball.xcor() == 330:
        ball.bounce_x()

    if ball.distance(r_paddle) < 60 and ball.xcor() == -330:
        ball.bounce_x()

    # detect when paddle misses
    if ball.xcor() > 400:   # right
        ball.reset_position()
        score_board.add_score_l()

    if ball.xcor() < -400:  # left
        ball.reset_position()
        score_board.add_score_r()

screen.exitonclick()
