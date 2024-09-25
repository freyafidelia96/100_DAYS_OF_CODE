from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.starting_speed = STARTING_MOVE_DISTANCE
        self.speed(self.starting_speed)
        self.penup()
        self.goto(random.randrange(-300, 300, 80), random.randrange(-240, 240, 80))
    

    def move(self):
        self.forward(MOVE_INCREMENT)

    
    
    
