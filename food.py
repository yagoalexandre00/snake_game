from turtle import Turtle
from random import randint, choice
FOOD_COLOR = ["orange", "red", "yellow"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color(choice(FOOD_COLOR))
        y_position = randint(-270, 270)
        x_position = randint(-370, 370)
        self.goto(x_position, y_position)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

    def change_position(self):
        y_position = randint(-270, 270)
        x_position = randint(-370, 370)
        self.color(choice(FOOD_COLOR))
        self.goto(x_position, y_position)
