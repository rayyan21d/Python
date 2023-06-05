from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SLEEP_TIME = 0.05

screen = Screen()
screen.title("Snake Game")
screen.setup(width=700,height=700)
screen.bgcolor("black")
screen.tracer(0)

# Create a snake body and move the snake
snake = Snake()
food=Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while (game_is_on):

    screen.update()
    time.sleep(SLEEP_TIME)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()
        
        
    #Detect collision with wall
    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        game_is_on = False
        scoreboard.game_over()
        
    #Detect collision with tail
    if snake.detect_collision():
        game_is_on = False
        scoreboard.game_over()       


screen.exitonclick()
