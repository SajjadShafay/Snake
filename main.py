from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)   # tracer is what was immediately updating the screen -- we turned it off so that all
# segments of the body would be updated on screen at once instead of one by one

player = Snake()
food = Food()
score = Score()

screen.listen()   # there is a loop going on behind the scenes within the turtle library
screen.onkeypress(key="Up", fun=player.up)
screen.onkeypress(key="Down", fun=player.down)
screen.onkeypress(key="Left", fun=player.left)
screen.onkeypress(key="Right", fun=player.right)

game_is_on = True
while game_is_on:
    screen.update()  # manually update the screen with new positions and segments
    time.sleep(0.1)  # control the speed of how quickly the screen updates. Game speed depends on this.
    player.move()

    # Detect collision with food.
    if player.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        player.extend()

    # Detect collision with wall.
    if player.head.xcor() > 280 or player.head.xcor() < -280 or player.head.ycor() > 280 or player.head.ycor() < -280:
        score.reset()
        player.reset()


    # Detect collision with tail.
    for segment in player.segments[1:]:
        if player.head.distance(segment) < 10:
            player.reset()
            score.reset()


screen.exitonclick()
