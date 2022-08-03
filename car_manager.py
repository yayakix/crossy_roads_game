COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager():
    def __init__(self):
        self.all_cars = []

    def make_car(self):
        random_chance = random.randint(0,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.speed('slow')
            new_car.goto(280, random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 3)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(5)
