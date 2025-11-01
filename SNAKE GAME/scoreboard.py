from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.highscore = self.get_highscore()
        self.write_score()



    def get_highscore(self):
        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read())
            return self.highscore


    def write_score(self):
        self.write(arg=f'Score: {self.score}    High Score: {self.highscore}', align=ALIGNMENT, font=FONT)


    def game_over(self):
        if self.score == self.highscore:
            self.write_highscore()
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        if self.score >= self.highscore:
            self.write_highscore()
            self.highscore = self.score
        self.write_score() 


    def write_highscore(self):
        with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))

