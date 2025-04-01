#Project description: First try to apply OOP on the famous snake game using the turtle module
    #Save and modify the highscore into a txt file
#From: FreedomOutlines
#Start: 05.03.2025 04:00 AM
#End: 06.03.2025 12:00 PM

from turtle import Screen
import snake
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# setting up a screen
new_screen = Screen()
new_screen.setup(width=600, height=600)
new_screen.bgcolor("black")
new_screen.title("Snack Game by FreedomOutlines")
new_screen.tracer(0)


snake1 = Snake()
food = Food()
scoreboard = ScoreBoard()


# setting up event listeners to move in all four direction
new_screen.listen()
new_screen.onkey(key="w", fun=snake1.north)
new_screen.onkey(key="d", fun=snake1.east)
new_screen.onkey(key="a", fun=snake1.west)
new_screen.onkey(key="s", fun=snake1.south)




game_is_on = True
while game_is_on:
    new_screen.update()
    time.sleep(0.07)
    snake1.move()

    # Detect collision with food. When the snake head touches the food, the food position will be refreshed
    if snake1.head.distance(food) < 15:
        food.refresh_position()
        snake1.create_a_segment()
        scoreboard.modify_score()

    # Detect collision with wall
    if snake1.head.xcor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake1.reset_snake()


    # Detect collision with Tail
    for segment in snake1.segments[1:]:
        if snake1.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake1.reset_snake()




new_screen.exitonclick()