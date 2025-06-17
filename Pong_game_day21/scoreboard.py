from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Capricon", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.update()

    def update(self):
        self.write(arg=f"{self.l_score}     {self.r_score}", align=ALIGNMENT, font=FONT)

    def add_score_r(self):
        self.r_score += 1
        self.clear()
        self.update()

    def add_score_l(self):
        self.l_score += 1
        self.clear()
        self.update()
