from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(1000, 1000)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_on:
    screen.update()
    time.sleep(0.1)

    for s in snake.segments[1:]:
        if snake.head.distance(s) == 0:
            scoreboard.end_game()
            game_on = False

    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.increment()
        snake.add_segment()

    if snake.head.xcor() >= 480 or snake.head.ycor() >= 480 or snake.head.xcor() <= -480 or snake.head.ycor() <= -480:
        scoreboard.end_game()
        game_on = False

    snake.move()

screen.exitonclick()
