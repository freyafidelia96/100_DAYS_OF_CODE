from turtle import *
import random

def moveForwards():
    newTurtle.forward(10)

def moveBackwards():
    newTurtle.backward(10)

def counterClockwise():
    newTurtle.left(10)

def clockwise():
    newTurtle.right(10)

def clear():
    newTurtle.clear()
    newTurtle.penup()
    newTurtle.home()
    newTurtle.pendown()

screen = Screen()
screen.listen()
screen.screensize(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yCordinates = 0

allTurtles = []

for turtleIndex in range(6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colors[turtleIndex])
    newTurtle.penup()
    newTurtle.goto(-230, yCordinates)
    newTurtle.pendown()
    yCordinates += 50
    allTurtles.append(newTurtle)

userBet = screen.textinput("Make a bet", "Which turtle will win the race? Enter a color: ")

if userBet:
    is_race_on = True
    
while is_race_on:
    for newTurtles in allTurtles:
        if newTurtles.xcor() > 230:
            is_race_on = False
            winningColor = newTurtles.pencolor()
            if winningColor == userBet:
                print(f"You've won! The {winningColor} turtle is the winner!")
            else:
                print(f"You've lost The {winningColor} turtle is the winner!")
            break
        newTurtles.penup()
        newTurtles.forward(random.randint(0, 10))





"""screen.onkey(key= "W", fun= moveForwards)
screen.onkey(key= "S", fun= moveBackwards)
screen.onkey(key= "A", fun= counterClockwise)
screen.onkey(key= "D", fun= clockwise)
screen.onkey(key= "C", fun= clear)

"""
screen.exitonclick()