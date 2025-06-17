from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Calibri", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        with open("data.txt") as highscore:
            self.highscore = int(highscore.read())
        self.goto(x=0, y=270)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"score: {self.score} : Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as highscore:
                highscore.write(str(self.score))
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update()
