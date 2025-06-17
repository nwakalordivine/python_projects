from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(x=-250, y=250)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Level: {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over_text(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over.", align="center", font=FONT)
