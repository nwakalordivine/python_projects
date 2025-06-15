from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Calibri", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0
        self.add_score()

    def add_score(self):
        self.write(arg=f"score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over_text(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over.", align="center", font=FONT)

    def clear_board(self):
        self.clear()

