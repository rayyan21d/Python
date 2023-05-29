from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=600)
user_bet= screen.textinput(title="Make your bet", prompt="Which  turtle will win the race? RED BLUE BLACK GREEN YELLOW")

is_race_on = False

#Initialize the turtle

def initialize_turtle(color):
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    return tim

#Setting the turtle position

def set_turtle_position(turtle, x, y):
    turtle.goto(x, y)

    
    
    
colors=["red", "green", "blue", "black", "yellow"]
racer_turtles = []

for i in range(5):
    racer_turtles.append(initialize_turtle(colors[i]))
    set_turtle_position(racer_turtles[i], -230, -200 + i*100)

  
if user_bet:
    is_race_on = True
      
  
  
while(is_race_on):
    
    for turtle in racer_turtles:
        
        if(turtle.xcor() > 230):
            winner_turtle = turtle.pencolor()
            is_race_on = False
            break
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
    
if(winner_turtle == user_bet):
    screen.title("You won!")
else:
    screen.title("You lost!")
    
    
    
      
screen.exitonclick()
    