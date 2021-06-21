from turtle import Turtle
from random import choice
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
RANDOM_COLOURS = ["blue", "red", "yellow", "white", "pink", "purple", "light blue", "gold", "light green", "orange",
                  "hot pink", "deep pink", "navy", "green yellow", "lawn green", "crimson", "black", "brown"]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            snake_body = Turtle(shape="square")
            snake_body.color(choice(RANDOM_COLOURS))
            snake_body.penup()
            snake_body.goto(position)
            self.body.append(snake_body)

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x_position = self.body[seg_num - 1].xcor()
            new_y_position = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x_position, new_y_position)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def cross_borders(self):
        current_x_position = self.body[0].xcor()
        current_y_position = self.body[0].ycor()

        if self.body[0].xcor() >= 400:
            self.body[0].goto(-400, current_y_position)
        elif self.body[0].xcor() <= -400:
            self.body[0].goto(400, current_y_position)
        if self.body[0].ycor() >= 300:
            self.body[0].goto(current_x_position, -300)
        elif self.body[0].ycor() <= -300:
            self.body[0].goto(current_x_position, 300)

    def increase_snake(self):
        x = self.body[-1].xcor()
        y = self.body[-1].ycor()
        extra_body = Turtle(shape="square")
        extra_body.color(choice(RANDOM_COLOURS))
        extra_body.penup()
        extra_body.goto(x, y)
        self.body.append(extra_body)
