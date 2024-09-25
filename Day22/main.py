from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
STARING_POSITIONS1 = (-350, 0)
STARING_POSITIONS2 = (350, 0)

screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
turtle = Turtle()
turtle.hideturtle()
turtle.speed("fastest")
turtle.color("white")
turtle.penup()
turtle.goto(0, -500)
turtle.setheading(90)
for i in range(50):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

pad1 = Paddle(STARING_POSITIONS1)
pad2 = Paddle(STARING_POSITIONS2)
ball = Ball()

screen = Screen()
screen.listen()
screen.onkey(pad1.up,"Up")
screen.onkey(pad1.down,"Down")
screen.onkey(pad2.up,"w")
screen.onkey(pad2.up,"s")
      

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)


    ball.move()

    if ball.ycor() > 300 and ball.ycor() < -300:
        ball.bounce()




screen.exitonclick()