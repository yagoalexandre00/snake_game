from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier New', 18, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-20, 270)
        self.hideturtle()
        with open("data.txt") as data_file:
            self.highscore = int(data_file.read())
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data_file:
                data_file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-20, 270)
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
