from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    score: int

    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboare()

    def read_highscore(self):
        with open("data.txt") as f:
            self.high_score = int(f.read())

    def write_highscore(self, score):
        with open("data.txt", mode="w") as f:
            f.write(str(self.score))
    def update_scoreboare(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboare()

    def reset(self):
        if self.score > self.high_score:
            self.write_highscore(self.score)
        self.score = 0
        self.read_highscore()
        self.update_scoreboare()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
