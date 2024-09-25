from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.x_move = self.y_move = 10



    def move(self):
        self.new_x = self.xcor() + self.x_move
        self.new_y = self.ycor() + self.y_move

        self.goto(self.new_x, self.new_y)


    def bounce(self):
        self.y_move *= -1
    
    """def bounce_back(self):
        #bounce back from heading left
        if self.ball.heading() >= 0 and self.ball.heading() <= 90 or self.ball.heading() >= 270 and self.ball.heading() <= 360:
            self.ball.setheading(self.ball.heading() + 180)
        
        #bounce back from heading left
        if self.ball.heading() >= 90 and self.ball.heading() <= 180 or self.ball.heading() >= 180 and self.ball.heading() <= 270:
            self.ball.setheading(self.ball.heading() + 180)
"""
