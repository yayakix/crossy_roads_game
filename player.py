STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import  Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('green')
        self.goto(0, -280)
        self.setheading(90)


    def move_forward(self):
        while True:
            self.goto(self.xcor(), self.ycor() - 10)


