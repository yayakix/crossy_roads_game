import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
# scoreboard = Scoreboard
car_manager = CarManager()

screen.onkey(player.move_forward, 'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.make_car()
    car_manager.move()




    screen.update()
