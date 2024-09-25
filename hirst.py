from turtle import *
import random
import turtle as t
t.colormode(255)

"""rgbColors = []
colors = colorgram.extract('download.jpeg', 20)
for color in colors:
    r = color.rgb.r
    g =  color.rgb.g
    b = color.rgb.b

    newColors = (r,g,b)
    rgbColors.append(newColors)
print(rgbColors)"""

colors = [(229, 227, 224), (227, 223, 225), (217, 226, 220), (195, 172, 122), (221, 226, 232), (159, 100, 58), (186, 161, 51), (126, 37, 25), (8, 54, 78), (52, 34, 29), (109, 70, 85), (118, 162, 175), (26, 119, 167), (74, 35, 43), (86, 139, 65), (9, 64, 44), (69, 153, 133), (121, 35, 40), (182, 98, 82), (209, 202, 146)]
tim = Turtle()
tim.speed("fastest")

yCoordinates = 0

for i in range(10):
    for i in range(10):
        tim.dot(15, random.choice(colors))
        tim.penup()
        tim.forward(40)
    yCoordinates += 40
    tim.goto(0, yCoordinates)
    tim.pendown()




screen = Screen()
screen.exitonclick()