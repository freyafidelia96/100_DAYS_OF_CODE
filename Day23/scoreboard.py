from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-280, 280)
        self.write(f"Level: {self.level}", "left", font=FONT)
        self.hideturtle()

    
    def increment_score(self):
        self.level += 1
        self.clear()
        self.goto(-280, 280)
        self.write(f"Level: {self.level}", "left", font=FONT)
    

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", "center", font=FONT)

        
