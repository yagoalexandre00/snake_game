from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Starts the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("dark green")
screen.title("Ssssnake Game")
screen.tracer(0)

tom = Snake()
food = Food()
score = Scoreboard()

game_is_on = True

while game_is_on:
    tom.move()
    tom.cross_borders()
    screen.update()

    if score.score <= 6:
        time.sleep(0.09)
    elif 6 < score.score <= 10:
        time.sleep(0.08)
    elif 10 < score.score <= 15:
        time.sleep(0.06)
    elif 15 < score.score <= 19:
        time.sleep(0.05)
    else:
        time.sleep(0.03)

    # Detect collision with food
    if tom.head.distance(food) < 17:
        food.change_position()
        score.increase_score()
        tom.increase_snake()

    for segments in tom.body[1:]:
        if tom.head.distance(segments) < 5:
            score.reset_scoreboard()
            tom.reset_snake()

    screen.listen()
    screen.onkey(fun=tom.left, key="Left")
    screen.onkey(fun=tom.right, key="Right")
    screen.onkey(fun=tom.up, key="Up")
    screen.onkey(fun=tom.down, key="Down")


screen.exitonclick()
