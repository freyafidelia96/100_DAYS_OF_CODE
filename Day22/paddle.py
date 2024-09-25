from turtle import Turtle, Screen
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, STARTING_POSITIONS):
        super().__init__()
        self.STARTING_POSITIONS = STARTING_POSITIONS
        self.create_paddle()
        

    def create_paddle(self):
        self.new_paddle = Turtle()
        self.new_paddle.shape("square")
        self.new_paddle.color("white")
        self.new_paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.new_paddle.penup()
        self.new_paddle.goto(self.STARTING_POSITIONS )


    def up(self):
        self.new_paddle.goto(self.new_paddle.xcor(), self.new_paddle.ycor() + MOVE_DISTANCE)

    def down(self):
        self.new_paddle.goto(self.new_paddle.xcor(), self.new_paddle.ycor() - MOVE_DISTANCE)


