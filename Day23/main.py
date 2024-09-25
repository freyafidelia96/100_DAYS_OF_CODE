import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

cars = []

for i in range(20):
    car = CarManager()
    cars.append(car)

def move_cars():
    for car in cars:
        if car.xcor() < -300:
            car.goto(300, random.randrange(-240, 260, 80))
        car.move()

        #detect if player hits the cars
        if player.distance(car) < 20:
            scoreboard.gameover()
            return False
    return True

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    screen.listen()
    screen.onkey(player.up, "u")

    #detect if it has crossed all hurdles
    if player.ycor() > 240:
        scoreboard.increment_score()
        player.restart()

    game_is_on = move_cars()

    screen.update()

        
screen.exitonclick()

    

