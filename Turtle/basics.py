import turtle as t
from random import *
tim = t.Turtle()

tim.shape("turtle")
t.colormode(cmode=255)
tim.speed("fastest")
tim.pensize(15)

direction = [0, 90, 180, 270]
n = 10000

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color = (r, g, b)
    return color


for i in range(n):
    
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(direction))
   
   
    
