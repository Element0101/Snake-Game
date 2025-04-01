from turtle import Turtle
FONT = ("arial", 18, "normal")
ALIGN = "center"
with open("data.txt", mode="r") as data:
    new_highscore = data.read()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.highscore = int(new_highscore)
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.update_score()


    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as new:
                new.write(str(self.highscore))
        self.score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", move=False, align=ALIGN, font=FONT)


    def modify_score(self):
        self.score += 1
        self.update_score()

