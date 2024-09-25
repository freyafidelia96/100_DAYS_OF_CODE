from turtle import Turtle, Screen
import random

timmyTurtle = Turtle()
colors = ["royal blue", "dark slate gray", "lime green", "olive", "dark goldenrod", "orange", "light salmon", "dark magenta", "magenta", "salmon"]
def drawShape(numSides):
    angle = 360/numSides

    for i in range(numSides):
        timmyTurtle.forward(100)
        timmyTurtle.right(angle)


def startDrawingShape():
    for i in range(3, 11):
        timmyTurtle.color(random.choice(colors))
        drawShape(i)

import turtle as t
t.colormode(255)
timmyTurtle.speed("fastest")

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return(r, g, b)

def startRandomWalk():
    directions = [0, 90, 180, 270]
    timmyTurtle.width(15)

    for i in range(200):
        timmyTurtle.color(randomColor())
        timmyTurtle.forward(30)
        timmyTurtle.setheading(random.choice(directions))

def spirograph():
    timmyTurtle.circle(70)
    timmyTurtle.left(5)

degree = 0
while degree != 360:
    timmyTurtle.color(randomColor())
    spirograph()
    degree += 5











screen = Screen()
screen.exitonclick()